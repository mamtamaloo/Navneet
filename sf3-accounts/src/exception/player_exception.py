from fastapi import status


class PlayerCreationException(Exception):
    def __init__(self, exception: str):
        self.exception = exception
        self.status_code = status.HTTP_400_BAD_REQUEST


class PlayerNotExistException(Exception):
    def __init__(self, name: str):
        self.name = name
        self.status_code = status.HTTP_404_NOT_FOUND
