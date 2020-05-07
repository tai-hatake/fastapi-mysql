from sqlalchemy import Column, Integer, String, Boolean
from api.db.base import Base
from api.db.session import engine


# userテーブルのモデルUserTableを定義
class User(Base):
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
