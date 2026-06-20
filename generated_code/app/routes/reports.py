from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi import status
from app.repositories import report_repository
from app.schemas import report
from app.services import report_service

router = APIRouter(
    prefix="/reports",
    tags=["reports"],
)

@router.get("/")
async def get_all_reports(report_repo: report_repository.ReportRepository = Depends()):
    reports = await report_repo.get_all()
    return JSONResponse(content=[report.Report.from_orm(r).dict() for r in reports], status_code=status.HTTP_200_OK)

@router.get("/{report_id}")
async def get_report_by_id(report_id: int, report_repo: report_repository.ReportRepository = Depends()):
    report_obj = await report_repo.get_by_id(report_id)
    if report_obj is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Report not found")
    return JSONResponse(content=report.Report.from_orm(report_obj).dict(), status_code=status.HTTP_200_OK)

@router.post("/")
async def create_report(report_data: report.ReportCreate, report_repo: report_repository.ReportRepository = Depends(), report_service: report_service.ReportService = Depends()):
    report_obj = await report_service.create_report(report_data)
    return JSONResponse(content=report.Report.from_orm(report_obj).dict(), status_code=status.HTTP_201_CREATED)

@router.put("/{report_id}")
async def update_report(report_id: int, report_data: report.ReportUpdate, report_repo: report_repository.ReportRepository = Depends(), report_service: report_service.ReportService = Depends()):
    report_obj = await report_repo.get_by_id(report_id)
    if report_obj is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Report not found")
    updated_report = await report_service.update_report(report_id, report_data)
    return JSONResponse(content=report.Report.from_orm(updated_report).dict(), status_code=status.HTTP_200_OK)

@router.delete("/{report_id}")
async def delete_report(report_id: int, report_repo: report_repository.ReportRepository = Depends(), report_service: report_service.ReportService = Depends()):
    report_obj = await report_repo.get_by_id(report_id)
    if report_obj is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Report not found")
    await report_service.delete_report(report_id)
    return JSONResponse(content={"message": "Report deleted successfully"}, status_code=status.HTTP_200_OK)