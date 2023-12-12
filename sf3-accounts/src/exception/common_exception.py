from fastapi import status


class SomethingWentWrongException(Exception):
    def __init__(self, error):
        self.error = error


class DataNotFoundException(Exception):
    def __init__(self):
        self.status_code = status.HTTP_404_NOT_FOUND
        self.detail = "data not found"


class InvalidDataException(Exception):
    def __init__(self, name: str):
        self.name = name
        self.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
