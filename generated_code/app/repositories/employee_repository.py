from sqlalchemy import select
from sqlalchemy.orm import Session
from generated_code.app.models.employee import Employee
from generated_code.app.schemas.employee import Employee as EmployeeSchema

class EmployeeRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return self.session.execute(select(Employee)).all()

    def get_by_id(self, id: int):
        return self.session.get(Employee, id)

    def create(self, employee: EmployeeSchema):
        new_employee = Employee(**employee.dict())
        self.session.add(new_employee)
        self.session.commit()
        self.session.refresh(new_employee)
        return new_employee

    def update(self, id: int, employee: EmployeeSchema):
        existing_employee = self.session.get(Employee, id)
        if existing_employee:
            existing_employee.name = employee.name
            existing_employee.email = employee.email
            self.session.commit()
            self.session.refresh(existing_employee)
            return existing_employee
        return None

    def delete(self, id: int):
        employee = self.session.get(Employee, id)
        if employee:
            self.session.delete(employee)
            self.session.commit()
            return True
        return False