from sqlalchemy import Column, Integer, String, Boolean
from api.db.base import Base
from api.db.session import engine


# userテーブルのモデルUserTableを定義
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(30), nullable=False)
    age = Column(Integer)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)


def main():
    # テーブルが存在しなければ、テーブルを作成
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    main()
