from sqlalchemy import select
from sqlalchemy.orm import Session
from generated_code.app.models import admin
from typing import List

class AdminRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[admin.Admin]:
        return self.session.execute(select(admin.Admin)).scalars().all()

    def get_by_id(self, id: int) -> admin.Admin:
        return self.session.get(admin.Admin, id)

    def create(self, admin_data: dict) -> admin.Admin:
        new_admin = admin.Admin(**admin_data)
        self.session.add(new_admin)
        self.session.commit()
        self.session.refresh(new_admin)
        return new_admin

    def update(self, id: int, admin_data: dict) -> admin.Admin:
        existing_admin = self.get_by_id(id)
        if existing_admin:
            for key, value in admin_data.items():
                setattr(existing_admin, key, value)
            self.session.commit()
            self.session.refresh(existing_admin)
            return existing_admin
        return None

    def delete(self, id: int) -> None:
        existing_admin = self.get_by_id(id)
        if existing_admin:
            self.session.delete(existing_admin)
            self.session.commit()