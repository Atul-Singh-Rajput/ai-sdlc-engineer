from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import employee
from app.schemas import employee_schema
from typing import List

class EmployeeRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_all_employees(self) -> List[employee_schema.Employee]:
        employees = self.db_session.execute(select(employee.Employee)).scalars().all()
        return [employee_schema.Employee.from_orm(e) for e in employees]

    def get_employee_by_id(self, id: int) -> employee_schema.Employee:
        employee_obj = self.db_session.execute(select(employee.Employee).where(employee.Employee.id == id)).scalar()
        if employee_obj:
            return employee_schema.Employee.from_orm(employee_obj)
        return None

    def create_employee(self, employee_data: employee_schema.EmployeeCreate) -> employee_schema.Employee:
        new_employee = employee.Employee(**employee_data.dict())
        self.db_session.add(new_employee)
        self.db_session.commit()
        self.db_session.refresh(new_employee)
        return employee_schema.Employee.from_orm(new_employee)

    def update_employee(self, id: int, employee_data: employee_schema.EmployeeUpdate) -> employee_schema.Employee:
        employee_obj = self.db_session.execute(select(employee.Employee).where(employee.Employee.id == id)).scalar()
        if employee_obj:
            for key, value in employee_data.dict(exclude_unset=True).items():
                setattr(employee_obj, key, value)
            self.db_session.commit()
            self.db_session.refresh(employee_obj)
            return employee_schema.Employee.from_orm(employee_obj)
        return None

    def delete_employee(self, id: int) -> bool:
        employee_obj = self.db_session.execute(select(employee.Employee).where(employee.Employee.id == id)).scalar()
        if employee_obj:
            self.db_session.delete(employee_obj)
            self.db_session.commit()
            return True
        return False