from typing import Any, List

from fastapi import APIRouter, Depends
from api.db.session import get_db, session
from api import models, schemas

router = APIRouter()

@router.get("/")
def read_users():
    """全ユーザ情報取得"""
    db = get_db()
    users = db.query(models.User).all()
    return users

@router.get("/{user_id}")
def read_user(user_id: int):
    """idでユーザ取得"""
    db = get_db()
    user = db.query(models.User).\
        filter(models.User.id == user_id).first()
    return user

@router.post("/")
async def create_user(name: str, age: int):
    """ユーザ登録"""
    db = get_db()
    user = models.User()
    user.name = name
    user.age = age
    db.add(user)
    db.commit()

@router.put("/")
async def update_users(users: List[schemas.User]):
    """複数ユーザー更新"""
    db = get_db()
    for new_user in users:
        user = db.query(models.User).\
            filter(models.User.id == new_user.id).first()
        user.name = new_user.name
        user.age = new_user.age
        db.commit()
