from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from api.config import get_settings

user_name = get_settings().MYSQL_USER
password = get_settings().MYSQL_PASSWORD
host = get_settings().DOCKER_DB_HOST
database_name = get_settings().MYSQL_DATABASE

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

