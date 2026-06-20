from pydantic import BaseModel
from datetime import date
from typing import Optional

class ReportBase(BaseModel):
    report_name: str
    report_date: date
    report_status: str

class ReportCreate(ReportBase):
    pass

class Report(ReportBase):
    id: int
    created_at: date
    updated_at: date

    class Config:
        orm_mode = True

class ReportUpdate(BaseModel):
    report_name: Optional[str]
    report_date: Optional[date]
    report_status: Optional[str]