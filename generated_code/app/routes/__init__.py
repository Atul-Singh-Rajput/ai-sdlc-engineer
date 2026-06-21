from fastapi import APIRouter
from generated_code.app.routes.employee_routes import employee_router
from generated_code.app.routes.report_routes import report_router
from generated_code.app.routes.auth_routes import auth_router

router = APIRouter()

router.include_router(employee_router, prefix="/employees", tags=["employees"])
router.include_router(report_router, prefix="/reports", tags=["reports"])
router.include_router(auth_router, prefix="/authentication", tags=["authentication"])