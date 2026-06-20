from pydantic import BaseModel
from datetime import date
from typing import Optional

class Employee(BaseModel):
    id: Optional[int]
    name: str
    email: str
    job_title: str
    date_of_birth: date

    class Config:
        orm_mode = True

class EmployeeCreate(BaseModel):
    name: str
    email: str
    job_title: str
    date_of_birth: date

class EmployeeUpdate(BaseModel):
    name: Optional[str]
    email: Optional[str]
    job_title: Optional[str]
    date_of_birth: Optional[date]