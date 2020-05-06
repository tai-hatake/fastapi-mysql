from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from api.config import settings

user_name = settings.mysql_user
password = settings.mysql_password
host = settings.docker_db_host
database_name = settings.mysql_database

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

session = scoped_session(
    # ORM実行時の設定。自動コミットするか、自動反映するか
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)


def get_db() -> Generator:
    try:
        return session
    finally:
        session.close()
