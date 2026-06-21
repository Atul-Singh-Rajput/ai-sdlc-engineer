from pydantic import BaseModel
from typing import Optional
from datetime import date

class Employee(BaseModel):
    id: Optional[int]
    name: str
    email: str
    job_title: str
    hire_date: date

    class Config:
        orm_mode = True

class EmployeeCreate(BaseModel):
    name: str
    email: str
    job_title: str
    hire_date: date

class EmployeeUpdate(BaseModel):
    name: Optional[str]
    email: Optional[str]
    job_title: Optional[str]
    hire_date: Optional[date]