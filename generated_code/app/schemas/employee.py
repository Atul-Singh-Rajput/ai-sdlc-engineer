from pydantic import BaseModel
from datetime import date
from typing import Optional

class Employee(BaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    email: str
    date_of_birth: date
    department_id: int

    class Config:
        orm_mode = True

class EmployeeCreate(Employee):
    pass

class EmployeeUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    date_of_birth: Optional[date]
    department_id: Optional[int]