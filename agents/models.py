from pydantic import BaseModel
from typing import List

class RequirementAnalysis(BaseModel):
    project_name: str
    project_type: str
    entities: List[str]
    roles: List[str]
    features: List[str]
    api_endpoints: List[str]