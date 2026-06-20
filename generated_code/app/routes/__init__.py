from fastapi import APIRouter

from . import employees
from . import admins
from . import reports

router = APIRouter()

router.include_router(
    employees.router,
    prefix="/employees",
    tags=["employees"]
)

router.include_router(
    admins.router,
    prefix="/admins",
    tags=["admins"]
)

router.include_router(
    reports.router,
    prefix="/reports",
    tags=["reports"]
)