from sqlalchemy.orm import Session
from app.models.admin import Admin
from app.schemas.admin import AdminCreate, AdminUpdate
from typing import List, Optional

class AdminRepository:
    def get_all(self, db: Session) -> List[Admin]:
        return db.query(Admin).all()

    def get_by_id(self, db: Session, admin_id: int) -> Optional[Admin]:
        return db.query(Admin).filter(Admin.id == admin_id).first()

    def create(self, db: Session, admin: AdminCreate) -> Admin:
        db_admin = Admin(**admin.dict())
        db.add(db_admin)
        db.commit()
        db.refresh(db_admin)
        return db_admin

    def update(self, db: Session, admin_id: int, admin: AdminUpdate) -> Optional[Admin]:
        db_admin = self.get_by_id(db, admin_id)
        if db_admin:
            for key, value in admin.dict(exclude_unset=True).items():
                setattr(db_admin, key, value)
            db.commit()
            db.refresh(db_admin)
        return db_admin

    def delete(self, db: Session, admin_id: int) -> Optional[Admin]:
        db_admin = self.get_by_id(db, admin_id)
        if db_admin:
            db.delete(db_admin)
            db.commit()
        return db_admin