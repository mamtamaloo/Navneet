from pydantic.env_settings import BaseSettings


class Settings(BaseSettings):
    mysql_root_password: str
    database_username: str
    database_password: str
    database_host: str
    database_port: str
    database_name: str
    database_driver: str
    workers: str
    docs_url: str = "/accounts/v1/docs"
    redoc_url: str = "/accounts/v1/redoc"
    openapi_url: str = "/accounts/v1/openapi.json"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
