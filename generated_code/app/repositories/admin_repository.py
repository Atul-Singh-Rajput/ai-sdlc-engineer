from sqlalchemy.orm import Session
from app.models import Admin
from app.schemas import AdminCreate, AdminUpdate
from typing import Optional, List

class AdminRepository:
    def get_admin(self, db: Session, admin_id: int):
        return db.query(Admin).filter(Admin.id == admin_id).first()

    def get_admins(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(Admin).offset(skip).limit(limit).all()

    def create_admin(self, db: Session, admin: AdminCreate):
        db_admin = Admin(**admin.dict())
        db.add(db_admin)
        db.commit()
        db.refresh(db_admin)
        return db_admin

    def update_admin(self, db: Session, admin_id: int, admin: AdminUpdate):
        db_admin = self.get_admin(db, admin_id)
        if db_admin:
            for key, value in admin.dict(exclude_unset=True).items():
                setattr(db_admin, key, value)
            db.commit()
            db.refresh(db_admin)
        return db_admin

    def delete_admin(self, db: Session, admin_id: int):
        db_admin = self.get_admin(db, admin_id)
        if db_admin:
            db.delete(db_admin)
            db.commit()
        return db_admin