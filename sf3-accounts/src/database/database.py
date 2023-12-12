import loguru
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.core.config import settings

SQLALCHEMY_DATABASE_URL = (
    settings.database_driver
    + "://"
    + settings.database_username
    + ":"
    + settings.database_password
    + "@"
    + settings.database_host
    + ":"
    + settings.database_port
    + "/"
    + settings.database_name
)

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False)
    Base = declarative_base()
    SessionLocal.configure(binds={Base: engine})
except Exception as e:
    loguru.logger.exception(e)
