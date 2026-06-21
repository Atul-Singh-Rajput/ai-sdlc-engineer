from fastapi import FastAPI
from generated_code.app.routes import employee_routes, report_routes, auth_routes
from generated_code.app.database import engine

app = FastAPI()

app.include_router(employee_routes.router, prefix="/employees")
app.include_router(report_routes.router, prefix="/reports")
app.include_router(auth_routes.router, prefix="/authentication")

@app.on_event("startup")
async def startup_event():
    await engine.dispose()

@app.on_event("shutdown")
async def shutdown_event():
    await engine.dispose()