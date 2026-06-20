from pydantic import BaseModel
from datetime import date
from typing import Optional

class ReportingBase(BaseModel):
    title: str
    description: str

class ReportingCreate(ReportingBase):
    pass

class Reporting(ReportingBase):
    id: int
    created_at: date
    updated_at: date

    class Config:
        orm_mode = True

class ReportingUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]