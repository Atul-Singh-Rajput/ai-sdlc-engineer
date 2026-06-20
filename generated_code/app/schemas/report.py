from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ReportBase(BaseModel):
    title: str
    description: str

class ReportCreate(ReportBase):
    pass

class ReportUpdate(ReportBase):
    title: Optional[str]
    description: Optional[str]

class Report(ReportBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True