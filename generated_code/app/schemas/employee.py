from pydantic import BaseModel
from datetime import date
from typing import Optional

class EmployeeSchema(BaseModel):
    id: Optional[int]
    name: str
    email: str
    job_title: str
    date_of_birth: date
    hire_date: date

    class Config:
        orm_mode = True

class EmployeeCreateSchema(BaseModel):
    name: str
    email: str
    job_title: str
    date_of_birth: date
    hire_date: date

class EmployeeUpdateSchema(BaseModel):
    name: Optional[str]
    email: Optional[str]
    job_title: Optional[str]
    date_of_birth: Optional[date]
    hire_date: Optional[date]