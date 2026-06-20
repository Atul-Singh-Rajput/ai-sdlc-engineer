from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import employees, admins, reports
from app.database import database

app = FastAPI()

app.include_router(employees.router)
app.include_router(admins.router)
app.include_router(reports.router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    await database.connect()

@app.on_event("shutdown")
async def shutdown_event():
    await database.disconnect()