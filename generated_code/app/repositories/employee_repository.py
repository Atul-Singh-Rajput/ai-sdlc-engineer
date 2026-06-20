from sqlalchemy import select
from sqlalchemy.orm import Session
from generated_code.app.models import Employee

class EmployeeRepository:
    def get_all(self, db: Session):
        return db.execute(select(Employee)).all()

    def get_by_id(self, db: Session, id: int):
        return db.execute(select(Employee).where(Employee.id == id)).first()

    def create(self, db: Session, employee: dict):
        new_employee = Employee(**employee)
        db.add(new_employee)
        db.commit()
        db.refresh(new_employee)
        return new_employee

    def update(self, db: Session, id: int, employee: dict):
        existing_employee = db.execute(select(Employee).where(Employee.id == id)).first()
        if existing_employee:
            existing_employee[0].name = employee.get('name')
            existing_employee[0].email = employee.get('email')
            db.commit()
            db.refresh(existing_employee[0])
            return existing_employee[0]
        return None

    def delete(self, db: Session, id: int):
        employee_to_delete = db.execute(select(Employee).where(Employee.id == id)).first()
        if employee_to_delete:
            db.delete(employee_to_delete[0])
            db.commit()
            return True
        return False