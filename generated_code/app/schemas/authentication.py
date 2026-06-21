from pydantic import BaseModel
from datetime import datetime

class Authentication(BaseModel):
    id: int
    username: str
    password: str
    created_at: datetime
    updated_at: datetime

class AuthenticationCreate(BaseModel):
    username: str
    password: str

class AuthenticationUpdate(BaseModel):
    username: str | None
    password: str | None

class AuthenticationResponse(BaseModel):
    id: int
    username: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True