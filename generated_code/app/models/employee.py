from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    department_id = Column(Integer, ForeignKey("departments.id"))
    department = relationship("Department", back_populates="employees")

    def __repr__(self):
        return f"Employee(id={self.id}, name='{self.name}', department_id={self.department_id})"

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    employees = relationship("Employee", back_populates="department")

    def __repr__(self):
        return f"Department(id={self.id}, name='{self.name}')"