import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


user_name = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')
host = os.getenv('DOCKER_DB_HOST')
database_name = os.getenv('MYSQL_DATABASE')

DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    user_name,
    password,
    host,
    database_name,
)

engine = create_engine(
    DATABASE,
    pool_pre_ping=True,
    encoding="utf-8",
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

# modelで使用する
Base = declarative_base()
# DB接続用のセッションクラス、インスタンスが作成されると接続する
Base.query = session.query_property()
