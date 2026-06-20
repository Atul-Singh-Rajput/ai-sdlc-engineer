from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app import schemas, models, repositories
from app.dependencies import get_db

router = APIRouter(
    prefix="/admins",
    tags=["admins"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def read_admins(db: Session = Depends(get_db)):
    admins = repositories.admin_repository.get_all_admins(db)
    return admins

@router.get("/{admin_id}")
def read_admin(admin_id: int, db: Session = Depends(get_db)):
    db_admin = repositories.admin_repository.get_admin(db, admin_id)
    if db_admin is None:
        raise HTTPException(status_code=404, detail="Admin not found")
    return db_admin

@router.post("/")
def create_admin(admin: schemas.AdminCreate, db: Session = Depends(get_db)):
    db_admin = repositories.admin_repository.get_admin_by_email(db, admin.email)
    if db_admin:
        raise HTTPException(status_code=400, detail="Email already registered")
    return repositories.admin_repository.create_admin(db, admin)

@router.put("/{admin_id}")
def update_admin(admin_id: int, admin: schemas.AdminUpdate, db: Session = Depends(get_db)):
    db_admin = repositories.admin_repository.get_admin(db, admin_id)
    if db_admin is None:
        raise HTTPException(status_code=404, detail="Admin not found")
    return repositories.admin_repository.update_admin(db, admin_id, admin)

@router.delete("/{admin_id}")
def delete_admin(admin_id: int, db: Session = Depends(get_db)):
    db_admin = repositories.admin_repository.get_admin(db, admin_id)
    if db_admin is None:
        raise HTTPException(status_code=404, detail="Admin not found")
    repositories.admin_repository.delete_admin(db, admin_id)
    return JSONResponse(status_code=200, content={"message": "Admin deleted successfully"})