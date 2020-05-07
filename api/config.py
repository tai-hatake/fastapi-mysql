from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
    MYSQL_DATABASE: str
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    DOCKER_DB_HOST: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SECRET_KEY: str
    class Config:
        env_file = '.env'


settings = Settings()
