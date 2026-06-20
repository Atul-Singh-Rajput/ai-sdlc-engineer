from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import date

Base = declarative_base()

class Reporting(Base):
    __tablename__ = 'reporting'

    id = Column(Integer, primary_key=True, index=True)
    report_name = Column(String)
    report_date = Column(Date, default=date.today())
    employee_id = Column(Integer, ForeignKey('employees.id'))
    department_id = Column(Integer, ForeignKey('departments.id'))
    employee = relationship('Employee', backref='reports')
    department = relationship('Department', backref='reports')

    def __repr__(self):
        return f'Reporting(id={self.id}, report_name={self.report_name}, report_date={self.report_date}, employee_id={self.employee_id}, department_id={self.department_id})'