from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from api.db.session import get_db
from api import models, schemas, logics
from api.config import settings

router = APIRouter()

@router.get("/", response_model=List[schemas.User])
def read_users():
    """全ユーザ情報取得"""
    db = get_db()
    users = db.query(models.User).all()
    print(schemas.User, users)
    return users

@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int):
    """idでユーザ取得"""
    db = get_db()
    user = db.query(models.User).\
        filter(models.User.id == user_id).first()
    return user

@router.post("/", response_model=schemas.User)
def create_user(
    *,
    user_in: schemas.UserCreate
) -> Any:
    """
    Create new user.
    """
    db = get_db()
    user = logics.user.get_by_email(db, email=user_in.email)
    print('get user', user)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = logics.user.create(db, obj_in=user_in)
    print('user', user)
    return user

@router.put("/", response_model=schemas.User)
async def update_users(users: List[schemas.User]):
    """複数ユーザー更新"""
    db = get_db()
    for new_user in users:
        user = db.query(models.User).\
            filter(models.User.id == new_user.id).first()
        user.name = new_user.name
        user.age = new_user.age
        db.commit()
