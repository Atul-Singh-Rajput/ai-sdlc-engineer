from pydantic import BaseModel
from datetime import datetime

class AdminBase(BaseModel):
    username: str
    email: str
    password: str

class AdminCreate(AdminBase):
    pass

class AdminUpdate(BaseModel):
    username: str | None = None
    email: str | None = None
    password: str | None = None

class Admin(AdminBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True