from pydantic import BaseModel
from typing import Optional

class Employee(BaseModel):
    id: Optional[int]
    name: str
    email: str
    department: str

    class Config:
        orm_mode = True

class EmployeeCreate(Employee):
    pass

class EmployeeUpdate(BaseModel):
    name: Optional[str]
    email: Optional[str]
    department: Optional[str]