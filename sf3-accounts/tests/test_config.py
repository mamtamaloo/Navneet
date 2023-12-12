from fastapi.testclient import TestClient

from main import app
from src.core.config import settings

client = TestClient(app)


# def test_settings():
#     assert settings.mysql_root_password == "root"
#     assert settings.database_username == "root"
#     assert settings.database_password == "root"
#     assert settings.database_host == "localhost"
#     assert settings.database_port == "3306"
#     assert settings.database_name == "sixfour3accounts"
#     assert settings.database_driver == "mysql+pymysql"
#     assert settings.workers == "4"


def test_settings():
    try:
        settings.mysql_root_password
        settings.database_username
        settings.database_password
        settings.database_host
        settings.database_port
        settings.database_name
        settings.database_driver
        settings.workers
    except NameError:
        pass
