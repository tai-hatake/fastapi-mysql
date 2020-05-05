from fastapi import APIRouter

from api.v1 import users
# from api.v1 import login, users

api_router = APIRouter()
# api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])