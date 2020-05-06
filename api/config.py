from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
    mysql_database: str
    mysql_user: str
    mysql_password: str
    docker_db_host: str
    class Config:
        env_file = '.env'


settings = Settings()
