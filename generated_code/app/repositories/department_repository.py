from sqlalchemy import select
from sqlalchemy.orm import Session
from generated_code.app.database import SessionLocal
from generated_code.app.models.department import Department

class DepartmentRepository:
    def __init__(self, session: Session = SessionLocal()):
        self.session = session

    def get_all(self):
        return self.session.execute(select(Department)).scalars().all()

    def get_by_id(self, id: int):
        return self.session.get(Department, id)

    def create(self, department: Department):
        self.session.add(department)
        self.session.commit()
        self.session.refresh(department)
        return department

    def update(self, id: int, department: Department):
        existing_department = self.get_by_id(id)
        if existing_department:
            existing_department.name = department.name
            self.session.commit()
            self.session.refresh(existing_department)
            return existing_department
        return None

    def delete(self, id: int):
        department = self.get_by_id(id)
        if department:
            self.session.delete(department)
            self.session.commit()
            return True
        return False