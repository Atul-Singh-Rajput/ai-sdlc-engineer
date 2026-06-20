from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AdminBase(BaseModel):
    username: str
    email: str

class AdminCreate(AdminBase):
    password: str

class AdminUpdate(AdminBase):
    password: Optional[str]

class Admin(AdminBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True