# from sqlalchemy import Boolean, Column, Integer, String
# from sqlalchemy.orm import relationship

# from app.db.base import Base


# class User(Base):
#     id = Column(Integer, primary_key=True, index=True)
#     full_name = Column(String, index=True)
#     email = Column(String, unique=True, index=True, nullable=False)
#     hashed_password = Column(String, nullable=False)
#     is_active = Column(Boolean(), default=True)
#     is_superuser = Column(Boolean(), default=False)

from sqlalchemy import Column, Integer, String, Boolean
from pydantic import BaseModel
from api.db.session import Base
from api.db.session import engine


# userテーブルのモデルUserTableを定義
class UserTable(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(30), nullable=False)
    age = Column(Integer)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)


# POSTやPUTのとき受け取るRequest Bodyのモデルを定義
class User(BaseModel):
    id: int
    name: str
    age: int
    full_name: str
    email: str
    hashed_password: str
    is_active: bool
    is_superuser: bool

def main():
    # テーブルが存在しなければ、テーブルを作成
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    main()
