from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ReportBase(BaseModel):
    title: str
    description: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class ReportCreate(ReportBase):
    pass

class ReportUpdate(ReportBase):
    title: Optional[str] = None
    description: Optional[str] = None

class Report(ReportBase):
    id: int
    class Config:
        orm_mode = True