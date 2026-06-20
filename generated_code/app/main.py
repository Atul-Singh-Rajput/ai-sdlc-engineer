from fastapi import FastAPI
from generated_code.app.routes import employees, admins, reports
from generated_code.app.database import engine

app = FastAPI()

app.include_router(employees.router, prefix="/employees", tags=["employees"])
app.include_router(admins.router, prefix="/admins", tags=["admins"])
app.include_router(reports.router, prefix="/reports", tags=["reports"])

@app.on_event("shutdown")
async def shutdown_event():
    await engine.dispose()