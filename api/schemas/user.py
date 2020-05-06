from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    age: int
    full_name: str
    email: str
    hashed_password: str
    is_active: bool
    is_superuser: bool
