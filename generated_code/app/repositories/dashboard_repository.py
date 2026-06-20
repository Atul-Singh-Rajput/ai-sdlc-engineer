from generated_code.app.models import Employee
from generated_code.app.utils.database import SessionLocal
from typing import List

class DashboardRepository:
    def __init__(self, db: SessionLocal):
        self.db = db

    def get_all_employees(self) -> List[Employee]:
        return self.db.query(Employee).all()

    def get_employee_by_id(self, employee_id: int) -> Employee:
        return self.db.query(Employee).filter(Employee.id == employee_id).first()

    def create_employee(self, employee: Employee) -> Employee:
        self.db.add(employee)
        self.db.commit()
        self.db.refresh(employee)
        return employee

    def update_employee(self, employee_id: int, employee: Employee) -> Employee:
        existing_employee = self.db.query(Employee).filter(Employee.id == employee_id).first()
        if existing_employee:
            existing_employee.name = employee.name
            existing_employee.department_id = employee.department_id
            self.db.commit()
            self.db.refresh(existing_employee)
            return existing_employee
        return None

    def delete_employee(self, employee_id: int) -> bool:
        employee = self.db.query(Employee).filter(Employee.id == employee_id).first()
        if employee:
            self.db.delete(employee)
            self.db.commit()
            return True
        return False