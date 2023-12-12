import loguru
from fastapi import Response, status

from src.exception.common_exception import SomethingWentWrongException
from src.exception.customer_exception import (
    CustomerCreationException,
    CustomerNotExistException,
)
from src.schemas import customer_schema
from src.utils.account_utils import parse_json


def create_customer(Customer):
    try:
        loguru.logger.debug("Customer has created successfully")
        headers = {"id": "PT001"}
        temp_dict = {"headers": headers, "status_code": status.HTTP_201_CREATED}
        return temp_dict

    except CustomerCreationException as e:
        loguru.logger.exception(e)
        raise CustomerCreationException(exception=str(e))


def get_customer(customer_id):
    try:
        json_file_path = "src/json/get_customer.json"  # read json file
        json_data = parse_json(json_file_path)
        for data in json_data:
            if data["id"] == customer_id:
                customer = customer_schema.GetCustomer(
                    id=data['id'],
                    first_name=data["firstName"],
                    last_name=data["lastName"],
                    email=data["email"],
                    user_group=data["userGroup"],
                    address=data["address"],
                    phone_number=data["phoneNumber"],
                    players=data["players"],
                )
                return customer
    except Exception as e:
        loguru.logger.exception(e)
        raise SomethingWentWrongException(error=str(e))
    else:
        raise CustomerNotExistException(name=customer_id)


def list_all_customers():
    try:
        json_file_path = "src/json/list_of_all_customers.json"
        json_data = parse_json(json_file_path)
        customer_list = []
        for data in json_data["customers"]:
            customer = customer_schema.AllCustomers(
                id=data['id'],
                first_name=data["firstName"],
                last_name=data["lastName"],
                email=data["email"],
                phone_number=data["phoneNumber"],
                players=data["players"],
            )
            customer_list.append(customer)
        return customer_schema.ListAllCustomers(customers=customer_list)
    except Exception as e:
        loguru.logger.exception(e)
        raise SomethingWentWrongException(error=str(e))


def update_customer(customer_id):
    try:
        json_file_path = "src/json/get_customer.json"
        json_data = parse_json(json_file_path)
        for data in json_data:
            if data["id"] == customer_id:
                return status.HTTP_200_OK
    except Exception as e:
        loguru.logger.exception(e)
        raise SomethingWentWrongException(error=str(e))
    else:
        raise CustomerNotExistException(name=customer_id)


def delete_customer(customer_id):
    try:
        json_file_path = "src/json/get_customer.json"
        json_data = parse_json(json_file_path)
        for data in json_data:
            if data["id"] == customer_id:
                return Response(status_code=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        loguru.logger.exception(e)
        raise SomethingWentWrongException(error=str(e))
    else:
        raise CustomerNotExistException(name=customer_id)
