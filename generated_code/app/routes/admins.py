from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import database
from app.repositories import admin_repository
from app.schemas import admin as admin_schema
from app.services import admin_service

router = APIRouter(
    prefix="/admins",
    tags=["admins"],
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[admin_schema.Admin])
def read_admins(db: Session = Depends(get_db)):
    admins = admin_repository.get_all(db)
    return admins

@router.get("/{admin_id}", response_model=admin_schema.Admin)
def read_admin(admin_id: int, db: Session = Depends(get_db)):
    db_admin = admin_repository.get_by_id(db, admin_id)
    if db_admin is None:
        raise HTTPException(status_code=404, detail="Admin not found")
    return db_admin

@router.post("/", response_model=admin_schema.Admin)
def create_admin(admin: admin_schema.AdminCreate, db: Session = Depends(get_db)):
    db_admin = admin_repository.get_by_email(db, admin.email)
    if db_admin:
        raise HTTPException(status_code=400, detail="Email already registered")
    return admin_repository.create(db, admin)

@router.put("/{admin_id}", response_model=admin_schema.Admin)
def update_admin(admin_id: int, admin: admin_schema.AdminUpdate, db: Session = Depends(get_db)):
    db_admin = admin_repository.get_by_id(db, admin_id)
    if db_admin is None:
        raise HTTPException(status_code=404, detail="Admin not found")
    return admin_repository.update(db, admin_id, admin)

@router.delete("/{admin_id}")
def delete_admin(admin_id: int, db: Session = Depends(get_db)):
    db_admin = admin_repository.get_by_id(db, admin_id)
    if db_admin is None:
        raise HTTPException(status_code=404, detail="Admin not found")
    admin_repository.delete(db, admin_id)
    return {"message": "Admin deleted successfully"}