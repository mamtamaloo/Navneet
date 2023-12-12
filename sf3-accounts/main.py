import pathlib

import toml
import uvicorn
from fastapi import FastAPI, Request, status
from starlette.responses import JSONResponse

from src.api.routes.v1 import customer, employee, health_check, player
from src.core.config import settings
from src.exception.common_exception import (
    DataNotFoundException,
    SomethingWentWrongException,
)
from src.exception.customer_exception import (
    CustomerCreationException,
    CustomerNotExistException,
)
from src.exception.employee_exception import (
    EmployeeCreationException,
    EmployeeExistException,
    EmployeeNotExistException,
)
from src.exception.player_exception import (
    PlayerCreationException,
    PlayerNotExistException,
)

pyproject_path = pathlib.Path("pyproject.toml")
version = toml.load(pyproject_path.open())

tags_metadata = [
    {"name": "Healthcheck"},
    {"name": "Employees"},
    {"name": "Customers"},
    {"name": "Players"},
]

app = FastAPI(
    title="SF3 Accounts API",
    version=version["tool"]["poetry"]["version"],
    docs_url=settings.docs_url,
    redoc_url=settings.redoc_url,
    openapi_url=settings.openapi_url,
    openapi_tags=tags_metadata,
)

app.include_router(health_check.router)
app.include_router(employee.router)
app.include_router(customer.router)
app.include_router(player.router)


@app.exception_handler(EmployeeExistException)
async def existing_employee_exception_handler(
    request: Request, exc: EmployeeExistException
):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": f"Employee already exist with this email id {exc.email}"},
    )


@app.exception_handler(DataNotFoundException)
async def data_not_found_exception_handler(
    request: Request, exc: DataNotFoundException
):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": "data not found"},
    )


@app.exception_handler(EmployeeCreationException)
async def employee_creation_exception_handler(
    request: Request, exc: EmployeeCreationException
):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": f"{exc.exception} employee has not created"},
    )


@app.exception_handler(EmployeeNotExistException)
async def not_existing_employee_exception_handler(
    request: Request, exc: EmployeeNotExistException
):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": f"employee id {exc.name}  not exist"},
    )


@app.exception_handler(CustomerCreationException)
async def customer_creation_exception_handler(
    request: Request, exc: CustomerCreationException
):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": f"{exc.exception} customer has not created"},
    )


@app.exception_handler(CustomerNotExistException)
async def not_existing_customer_exception_handler(
    request: Request, exc: CustomerNotExistException
):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": f"customer id {exc.name}  not exist"},
    )


@app.exception_handler(PlayerCreationException)
async def player_creation_exception_handler(
    request: Request, exc: PlayerCreationException
):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": f"{exc.exception} player has not created"},
    )


@app.exception_handler(PlayerNotExistException)
async def not_existing_player_exception_handler(
    request: Request, exc: PlayerNotExistException
):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": f" player id {exc.name}  not exist"},
    )


@app.exception_handler(SomethingWentWrongException)
async def something_went_wrong_exception_handler(
    request: Request, exc: SomethingWentWrongException
):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": f"{exc.error} something went wrong"},
    )


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
