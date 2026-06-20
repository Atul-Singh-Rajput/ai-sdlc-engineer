from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from app.repositories import report_repository
from app.schemas import report as report_schema
from app.models import report as report_model
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()

@router.get("/reports/", response_model=List[report_schema.Report])
async def read_reports(
    db: Session = Depends(report_repository.get_db)
):
    reports = report_repository.get_reports(db)
    return reports

@router.get("/reports/{report_id}", response_model=report_schema.Report)
async def read_report(
    report_id: int,
    db: Session = Depends(report_repository.get_db)
):
    report = report_repository.get_report(db, report_id)
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return report

@router.post("/reports/", response_model=report_schema.Report)
async def create_report(
    report: report_schema.ReportCreate,
    db: Session = Depends(report_repository.get_db)
):
    return report_repository.create_report(db, report)

@router.put("/reports/{report_id}", response_model=report_schema.Report)
async def update_report(
    report_id: int,
    report: report_schema.ReportUpdate,
    db: Session = Depends(report_repository.get_db)
):
    updated_report = report_repository.update_report(db, report_id, report)
    if updated_report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return updated_report

@router.delete("/reports/{report_id}")
async def delete_report(
    report_id: int,
    db: Session = Depends(report_repository.get_db)
):
    report_repository.delete_report(db, report_id)
    return JSONResponse(status_code=200, content={"message": "Report deleted successfully"})