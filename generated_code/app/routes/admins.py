from fastapi import APIRouter, Depends, HTTPException
from generated_code.app.repositories import admin_repository
from generated_code.app.schemas import admin as schemas
from generated_code.app.models import admin as models
from typing import List

router = APIRouter(
    prefix="/admins",
    tags=["admins"],
)

@router.get("/", response_model=List[schemas.Admin])
async def get_all_admins(admin_repo: admin_repository.AdminRepository = Depends()):
    return admin_repo.get_all()

@router.get("/{admin_id}", response_model=schemas.Admin)
async def get_admin_by_id(admin_id: int, admin_repo: admin_repository.AdminRepository = Depends()):
    admin = admin_repo.get_by_id(admin_id)
    if admin is None:
        raise HTTPException(status_code=404, detail="Admin not found")
    return admin

@router.post("/", response_model=schemas.Admin)
async def create_admin(admin: schemas.AdminCreate, admin_repo: admin_repository.AdminRepository = Depends()):
    return admin_repo.create(admin)

@router.put("/{admin_id}", response_model=schemas.Admin)
async def update_admin(admin_id: int, admin: schemas.AdminUpdate, admin_repo: admin_repository.AdminRepository = Depends()):
    admin_db = admin_repo.get_by_id(admin_id)
    if admin_db is None:
        raise HTTPException(status_code=404, detail="Admin not found")
    return admin_repo.update(admin_id, admin)

@router.delete("/{admin_id}")
async def delete_admin(admin_id: int, admin_repo: admin_repository.AdminRepository = Depends()):
    admin_db = admin_repo.get_by_id(admin_id)
    if admin_db is None:
        raise HTTPException(status_code=404, detail="Admin not found")
    admin_repo.delete(admin_id)
    return {"message": "Admin deleted successfully"}