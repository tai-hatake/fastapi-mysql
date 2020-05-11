from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from api.common import get_db
from api import models, schemas, logics
from api.config import settings
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/", response_model=List[schemas.User])
def read_users(
    db: Session = Depends(get_db)
):
    """全ユーザ情報取得"""
    users = db.query(models.User).all()
    return users

@router.get("/{user_id}", response_model=schemas.User)
def read_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    """idでユーザ取得"""
    user = db.query(models.User).\
        filter(models.User.id == user_id).first()
    return user

@router.post("/", response_model=schemas.User)
def create_user(
    db: Session = Depends(get_db),
    *,
    user_in: schemas.UserCreate
) -> Any:
    """
    Create new user.
    """
    user = logics.user.get_by_email(db, email=user_in.email)
    print('get user', user)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = logics.user.create(db, obj_in=user_in)
    return user

@router.put("/", response_model=schemas.User)
async def update_users(
    users: List[schemas.User],
    db: Session = Depends(get_db)
):
    """複数ユーザー更新"""
    for new_user in users:
        user = db.query(models.User).\
            filter(models.User.id == new_user.id).first()
        user.name = new_user.name
        user.age = new_user.age
        db.commit()
