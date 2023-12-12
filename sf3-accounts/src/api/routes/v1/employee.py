from typing import Optional, Union

from fastapi import APIRouter, Query, Response
from starlette import status

from src.constants.constants import ALPHABETS
from src.crud import employee_crud
from src.schemas.employee_schema import EmployeeCreate, UpdateEmployee

router = APIRouter(prefix="/accounts/v1/employees")


@router.post("", tags=["Employees"], status_code=status.HTTP_201_CREATED)
async def create_employee(employee: EmployeeCreate):
    emp_dict = employee_crud.create_employee(employee)
    if emp_dict["status_code"] == status.HTTP_201_CREATED:
        return Response(
            status_code=status.HTTP_201_CREATED, headers=emp_dict["headers"]
        )


@router.get("/{employee_id}", tags=["Employees"], status_code=status.HTTP_200_OK)
async def get_employee(employee_id: str, response: Response):
    return employee_crud.get_employee(employee_id)


@router.get("", tags=["Employees"], status_code=status.HTTP_200_OK)
async def list_all_employees(
    name: Optional[str] = Query(
        None,
        title="employee name",
        description="search employee using name",
        regex=ALPHABETS,
    ),
    status: Optional[str] = Query(
        default="ACTIVE",
        description="search by status",
    ),
    sort: Optional[str] = Query(None, description="sort the employee using name only"),
    limit: Union[int, None] = 20,
    offset: Union[int, None] = 0,
):
    employee_list = employee_crud.list_all_employees(name, status, sort)
    return employee_list


@router.put("/{employee_id}", tags=["Employees"], status_code=status.HTTP_200_OK)
async def update_employee(employee_id: str, employee: UpdateEmployee):
    employee = employee_crud.update_employee(employee_id)
    if employee == status.HTTP_200_OK:
        return Response(status_code=status.HTTP_200_OK)


@router.delete(
    "/{employee_id}",
    tags=["Employees"],
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_employee(employee_id: str):
    employee_status = employee_crud.delete_employee(employee_id)
    if employee_status == status.HTTP_204_NO_CONTENT:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
