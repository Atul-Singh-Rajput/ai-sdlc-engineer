from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from app import models
from app.repositories import admin_repository
from app.services import admin_service
from app.schemas import admin as admin_schema

router = APIRouter(tags=["admins"])

@router.post("/admins/", response_model=admin_schema.AdminResponse)
async def create_admin(admin: admin_schema.AdminCreate):
    db = admin_repository.get_db()
    existing_admin = admin_repository.get_admin_by_email(db, admin.email)
    if existing_admin:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    new_admin = admin_service.create_admin(db, admin)
    return new_admin

@router.get("/admins/", response_model=list[admin_schema.AdminResponse])
async def read_admins():
    db = admin_repository.get_db()
    admins = admin_repository.get_all_admins(db)
    return admins

@router.get("/admins/{admin_id}", response_model=admin_schema.AdminResponse)
async def read_admin(admin_id: int):
    db = admin_repository.get_db()
    admin = admin_repository.get_admin(db, admin_id)
    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Admin not found")
    return admin

@router.put("/admins/{admin_id}", response_model=admin_schema.AdminResponse)
async def update_admin(admin_id: int, admin: admin_schema.AdminUpdate):
    db = admin_repository.get_db()
    existing_admin = admin_repository.get_admin(db, admin_id)
    if not existing_admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Admin not found")
    updated_admin = admin_service.update_admin(db, admin_id, admin)
    return updated_admin

@router.delete("/admins/{admin_id}")
async def delete_admin(admin_id: int):
    db = admin_repository.get_db()
    admin = admin_repository.get_admin(db, admin_id)
    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Admin not found")
    admin_repository.delete_admin(db, admin_id)
    return {"message": "Admin deleted successfully"}

@router.post("/token", response_model=admin_schema.Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db = admin_repository.get_db()
    admin = admin_repository.get_admin_by_email(db, form_data.username)
    if not admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
    if not admin_service.verify_password(form_data.password, admin.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
    access_token = admin_service.create_access_token(data={"sub": admin.email})
    return {"access_token": access_token, "token_type": "bearer"}