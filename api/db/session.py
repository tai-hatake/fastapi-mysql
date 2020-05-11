from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from api.config import settings

user_name = settings.MYSQL_USER
password = settings.MYSQL_PASSWORD
host = settings.DOCKER_DB_HOST
database_name = settings.MYSQL_DATABASE

DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    user_name,
    password,
    host,
    database_name,
)

engine = create_engine(
    DATABASE,
    pool_pre_ping=True,
    encoding='utf-8',
    echo=True
)
sessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

