import loguru
from fastapi import status

from src.exception.common_exception import SomethingWentWrongException
from src.exception.employee_exception import (
    EmployeeCreationException,
    EmployeeNotExistException,
)
from src.schemas import employee_schema
from src.utils.account_utils import parse_json

emp = []


def create_employee(employee):
    try:
        loguru.logger.debug("employee has created successfully")
        headers = {"id": "EMP001"}
        temp_dict = {"headers": headers, "status_code": status.HTTP_201_CREATED}
        return temp_dict
    except EmployeeCreationException as e:
        loguru.logger.exception(e)
        raise EmployeeCreationException(exception=str(e))


def list_all_employees(name, status, sort):
    try:
        json_file_path = "src/json/list_employee.json"
        json_data = parse_json(json_file_path)
        emp_list = []
        for data in json_data["employees"]:
            emp_data = employee_schema.EmployeeListSchema(
                id=data["id"],
                first_name=data["firstName"],
                last_name=data["lastName"],
                email=data["email"],
                address=data["address"],
                primary_contact_number=data["primaryContactNumber"],
                creation_date=data["creationDate"],
                status=data["status"],
            )
            emp_list.append(emp_data)
        return employee_schema.EmployeeList(employee=emp_list)
    except Exception as e:
        loguru.logger.exception(e)
        raise SomethingWentWrongException(error=str(e))


def get_employee(employee_id):
    try:
        json_file_path = "src/json/get_employee.json"  # read json file
        employee_data = parse_json(json_file_path)
        for data in employee_data:
            if data["id"] == employee_id:
                emp_temp = employee_schema.UpdateEmployee(
                    id=data["id"],
                    first_name=data["firstName"],
                    last_name=data["lastName"],
                    email=data["email"],
                    user_group=data["userGroup"],
                    email_notifications=data["emailNotifications"],
                    address=data["address"],
                    contact=data["contact"],
                    profilePhotoS3Url=data["profilePhotoS3Url"],
                    gender=data["gender"],
                    description=data["description"],
                    experience=data["experience"],
                    start_date=data["startDate"],
                    rate=data["rate"],
                    status=data["status"],
                    locations=data["locations"],
                    services=data["services"],
                    working_hours=data["workingHours"],
                )
                return emp_temp
    except Exception as e:
        loguru.logger.exception(e)
        raise SomethingWentWrongException(error=str(e))
    else:
        raise EmployeeNotExistException(name=employee_id)


def update_employee(employee_id):
    try:
        json_file_path = "src/json/list_employee.json"
        json_data = parse_json(json_file_path)
        for data in json_data["employees"]:
            if data["id"] == employee_id:
                return status.HTTP_200_OK
    except Exception as e:
        loguru.logger.exception(e)
        raise SomethingWentWrongException(error=str(e))
    else:
        raise EmployeeNotExistException(name=employee_id)


def delete_employee(employee_id):
    try:
        json_file_path = "src/json/list_employee.json"
        json_data = parse_json(json_file_path)
        for data in json_data["employees"]:
            if data["id"] == employee_id:
                return status.HTTP_204_NO_CONTENT
    except Exception as e:
        loguru.logger.exception(e)
        raise SomethingWentWrongException(error=str(e))
    else:
        raise EmployeeNotExistException(name=employee_id)
