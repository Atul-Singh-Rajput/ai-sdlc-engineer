from typing import List
from pydantic import BaseModel
from generated_code.app.models import Employee, Admin, Report

class EmployeeSchema(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True

class AdminSchema(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True

class ReportSchema(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True