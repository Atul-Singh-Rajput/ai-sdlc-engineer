from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from generated_code.app.models.employee import Employee
from typing import List

class EmployeeRepository:
    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)

    def get_all(self) -> List[Employee]:
        session = self.Session()
        try:
            return session.query(Employee).all()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def get_by_id(self, id: int) -> Employee:
        session = self.Session()
        try:
            return session.query(Employee).filter_by(id=id).first()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def create(self, employee: Employee) -> Employee:
        session = self.Session()
        try:
            session.add(employee)
            session.commit()
            return employee
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def update(self, id: int, employee: Employee) -> Employee:
        session = self.Session()
        try:
            existing_employee = session.query(Employee).filter_by(id=id).first()
            if existing_employee:
                existing_employee.name = employee.name
                existing_employee.email = employee.email
                session.commit()
                return existing_employee
            else:
                raise ValueError("Employee not found")
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def delete(self, id: int) -> None:
        session = self.Session()
        try:
            employee = session.query(Employee).filter_by(id=id).first()
            if employee:
                session.delete(employee)
                session.commit()
            else:
                raise ValueError("Employee not found")
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()