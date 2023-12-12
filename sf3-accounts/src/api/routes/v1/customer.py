from typing import Optional, Union

from fastapi import APIRouter, Query, Response
from pydantic import EmailStr
from starlette import status

from src.constants.constants import SEARCH_WITH_NAME_OR_PHONE_NUMBER
from src.crud import customer_crud
from src.schemas.customer_schema import CustomerCreate, UpdateCustomer

router = APIRouter(prefix="/accounts/v1/customers")
emp = []


@router.post("", tags=["Customers"], status_code=status.HTTP_201_CREATED)
async def create_customer(customer: CustomerCreate):
    customer_dict = customer_crud.create_customer(customer)
    if customer_dict["status_code"] == status.HTTP_201_CREATED:
        return Response(
            status_code=status.HTTP_201_CREATED, headers=customer_dict["headers"]
        )


@router.get("/{customer_id}", tags=["Customers"], status_code=status.HTTP_200_OK)
async def get_customer(customer_id: str):
    customer = customer_crud.get_customer(customer_id)
    return customer


@router.get("", tags=["Customers"], status_code=status.HTTP_200_OK)
async def list_customers(
    search: Union[str, EmailStr, None] = Query(
        None,
        regex=SEARCH_WITH_NAME_OR_PHONE_NUMBER,
        description="search the customer using name,email or phone number",
    ),
    status: Union[str, None] = Query(default="ACTIVE"),
    membership: Union[str, None] = Query(
        None, description="filter the customer by membership"
    ),
    sort: Optional[str] = Query(
        None,
        description="sort the customer using name only",
    ),
    limit: Union[int, None] = 20,
    offset: Union[int, None] = 0,
):
    customer_list = customer_crud.list_all_customers()
    return customer_list


@router.delete(
    "/{customer_id}",
    tags=["Customers"],
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_customer(customer_id: str):
    return customer_crud.delete_customer(customer_id)


@router.put("/{customer_id}", tags=["Customers"], status_code=status.HTTP_200_OK)
async def update_customer(customer_id: str, customer: UpdateCustomer):
    customer = customer_crud.update_customer(customer_id)
    if customer == status.HTTP_200_OK:
        return Response(status_code=status.HTTP_200_OK)
