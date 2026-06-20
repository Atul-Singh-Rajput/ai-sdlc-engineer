from pydantic import BaseModel
from datetime import datetime

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    password: str

class Authentication(BaseModel):
    username: str
    password: str

class AuthenticationResponse(BaseModel):
    token: Token
    user: User