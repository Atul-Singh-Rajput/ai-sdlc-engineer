from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from generated_code.app.utils.database import engine
from generated_code.app.models.employee import Employee
from generated_code.app.schemas.employee import Employee as EmployeeSchema
from generated_code.app.schemas.auth import Auth

class AuthRepository:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Employee).all()

    def get_by_id(self, id):
        return self.session.query(Employee).filter_by(id=id).first()

    def create(self, employee: EmployeeSchema):
        db_employee = Employee(**employee.dict())
        self.session.add(db_employee)
        self.session.commit()
        self.session.refresh(db_employee)
        return db_employee

    def update(self, id, employee: EmployeeSchema):
        db_employee = self.get_by_id(id)
        if db_employee:
            db_employee.name = employee.name
            db_employee.email = employee.email
            self.session.commit()
            self.session.refresh(db_employee)
            return db_employee
        return None

    def delete(self, id):
        db_employee = self.get_by_id(id)
        if db_employee:
            self.session.delete(db_employee)
            self.session.commit()
            return True
        return False

    def authenticate(self, auth: Auth):
        return self.session.query(Employee).filter_by(email=auth.email, password=auth.password).first()