from pydantic import BaseModel
from typing import Optional

class Department(BaseModel):
    id: Optional[int]
    name: str
    description: Optional[str]

    class Config:
        orm_mode = True

class DepartmentCreate(Department):
    pass

class DepartmentUpdate(Department):
    name: Optional[str]
    description: Optional[str]