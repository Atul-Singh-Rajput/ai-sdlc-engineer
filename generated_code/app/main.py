from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from generated_code.app.routes import employees, admins, reports
from generated_code.app.database import engine

app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(employees.router, prefix="/employees", tags=["employees"])
app.include_router(admins.router, prefix="/admins", tags=["admins"])
app.include_router(reports.router, prefix="/reports", tags=["reports"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}