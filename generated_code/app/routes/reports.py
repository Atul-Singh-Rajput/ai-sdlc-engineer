from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi import status
from app.schemas.report import ReportSchema, ReportResponseSchema
from app.services.report_service import ReportService
from app.repositories.report_repository import ReportRepository
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter(prefix="/reports", tags=["reports"])

@router.get("/", response_model=list[ReportResponseSchema])
async def get_all_reports(db: Session = Depends(get_db)):
    report_service = ReportService(ReportRepository(db))
    return report_service.get_all_reports()

@router.get("/{report_id}", response_model=ReportResponseSchema)
async def get_report(report_id: int, db: Session = Depends(get_db)):
    report_service = ReportService(ReportRepository(db))
    report = report_service.get_report(report_id)
    if not report:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Report not found")
    return report

@router.post("/", response_model=ReportResponseSchema)
async def create_report(report: ReportSchema, db: Session = Depends(get_db)):
    report_service = ReportService(ReportRepository(db))
    return report_service.create_report(report)

@router.put("/{report_id}", response_model=ReportResponseSchema)
async def update_report(report_id: int, report: ReportSchema, db: Session = Depends(get_db)):
    report_service = ReportService(ReportRepository(db))
    existing_report = report_service.get_report(report_id)
    if not existing_report:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Report not found")
    return report_service.update_report(report_id, report)

@router.delete("/{report_id}")
async def delete_report(report_id: int, db: Session = Depends(get_db)):
    report_service = ReportService(ReportRepository(db))
    report = report_service.get_report(report_id)
    if not report:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Report not found")
    report_service.delete_report(report_id)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Report deleted successfully"})