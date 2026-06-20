from sqlalchemy import select
from sqlalchemy.orm import Session
from generated_code.app.models.employee import Employee
from generated_code.app.schemas.employee import Employee as EmployeeSchema

class EmployeeRepository:
    def get_all(self, db: Session):
        return db.execute(select(Employee)).all()

    def get_by_id(self, db: Session, employee_id: int):
        return db.execute(select(Employee).where(Employee.id == employee_id)).first()

    def create(self, db: Session, employee: EmployeeSchema):
        db_employee = Employee(**employee.dict())
        db.add(db_employee)
        db.commit()
        db.refresh(db_employee)
        return db_employee

    def update(self, db: Session, employee_id: int, employee: EmployeeSchema):
        db_employee = db.execute(select(Employee).where(Employee.id == employee_id)).first()
        if db_employee:
            db_employee[0].name = employee.name
            db_employee[0].email = employee.email
            db.commit()
            db.refresh(db_employee[0])
            return db_employee[0]
        return None

    def delete(self, db: Session, employee_id: int):
        db_employee = db.execute(select(Employee).where(Employee.id == employee_id)).first()
        if db_employee:
            db.delete(db_employee[0])
            db.commit()
            return True
        return False