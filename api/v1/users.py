from typing import Any, List

from fastapi import APIRouter
from api.db.session import session
from api.models.user import UserTable, User

router = APIRouter()

@router.get("/")
def read_users():
    """全ユーザ情報取得"""
    users = session.query(UserTable).all()
    return users

@router.get("/{user_id}")
def read_user(user_id: int):
    """idでユーザ取得"""
    user = session.query(UserTable).\
        filter(UserTable.id == user_id).first()
    return user

@router.post("/")
async def create_user(name: str, age: int):
    """ユーザ登録"""
    user = UserTable()
    user.name = name
    user.age = age
    session.add(user)
    session.commit()

@router.put("/")
async def update_users(users: List[User]):
    """複数ユーザー更新"""
    for new_user in users:
        user = session.query(UserTable).\
            filter(UserTable.id == new_user.id).first()
        user.name = new_user.name
        user.age = new_user.age
        session.commit()
