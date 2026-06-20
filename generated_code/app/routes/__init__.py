from fastapi import APIRouter
from generated_code.app.routes.employees import router as employees_router
from generated_code.app.routes.departments import router as departments_router
from generated_code.app.routes.reporting import router as reporting_router
from generated_code.app.routes.auth import router as auth_router

router = APIRouter()
router.include_router(employees_router, prefix="/employees", tags=["employees"])
router.include_router(departments_router, prefix="/departments", tags=["departments"])
router.include_router(reporting_router, prefix="/reporting", tags=["reporting"])
router.include_router(auth_router, prefix="/authentication", tags=["authentication"])