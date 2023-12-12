from fastapi import status


class EmployeeCreationException(Exception):
    def __init__(self, exception: str):
        self.exception = exception
        self.status_code = status.HTTP_400_BAD_REQUEST


class EmployeeExistException(Exception):
    def __init__(self, email: str):
        self.email = email
        self.status_code = status.HTTP_409_CONFLICT


class EmployeeNotExistException(Exception):
    def __init__(self, name: str):
        self.name = name
        self.status_code = status.HTTP_404_NOT_FOUND
