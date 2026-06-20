from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from generated_code.app.utils.security import get_password_hash, verify_password
from generated_code.app.repositories.auth_repository import AuthRepository
from generated_code.app.utils.database import get_db

router = APIRouter()

class User(BaseModel):
    username: str
    email: str
    full_name: str
    disabled: bool

class UserInDB(User):
    password: str

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db = next(get_db())
    auth_repository = AuthRepository(db)
    user = auth_repository.get_user_by_username(form_data.username)
    if not user:
        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"access_token": user.username, "token_type": "bearer"}

@router.post("/register")
async def register(user: User):
    db = next(get_db())
    auth_repository = AuthRepository(db)
    if auth_repository.get_user_by_username(user.username):
        raise HTTPException(
            status_code=400,
            detail="Username already exists",
        )
    hashed_password = get_password_hash(user.username)
    auth_repository.create_user(user.username, hashed_password, user.email, user.full_name)
    return {"message": "User created successfully"}