from pydantic import BaseModel
from typing import Optional, List
from datetime import date

class DashboardEmployeeSchema(BaseModel):
    id: int
    name: str
    department: str
    date_of_birth: date
    date_of_joining: date

class DashboardDepartmentSchema(BaseModel):
    id: int
    name: str
    total_employees: int

class DashboardSchema(BaseModel):
    total_employees: int
    total_departments: int
    employees: List[DashboardEmployeeSchema]
    departments: List[DashboardDepartmentSchema]

class DashboardFilterSchema(BaseModel):
    department_id: Optional[int]
    date_of_joining: Optional[date]