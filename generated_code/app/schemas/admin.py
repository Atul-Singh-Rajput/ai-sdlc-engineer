from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AdminBase(BaseModel):
    username: str
    email: str
    password: str

class AdminCreate(AdminBase):
    pass

class AdminUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

class Admin(AdminBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True