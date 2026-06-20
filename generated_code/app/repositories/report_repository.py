from sqlalchemy import select
from sqlalchemy.orm import Session
from generated_code.app.models.report import Report
from generated_code.app.schemas.report import ReportSchema
from typing import List

class ReportRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[ReportSchema]:
        reports = self.session.execute(select(Report)).all()
        return [ReportSchema.from_orm(report[0]) for report in reports]

    def get_by_id(self, report_id: int) -> ReportSchema:
        report = self.session.get(Report, report_id)
        return ReportSchema.from_orm(report) if report else None

    def create(self, report: ReportSchema) -> ReportSchema:
        new_report = Report(**report.dict())
        self.session.add(new_report)
        self.session.commit()
        self.session.refresh(new_report)
        return ReportSchema.from_orm(new_report)

    def update(self, report_id: int, report: ReportSchema) -> ReportSchema:
        existing_report = self.get_by_id(report_id)
        if existing_report:
            existing_report_dict = existing_report.dict()
            existing_report_dict.update(report.dict())
            updated_report = Report(**existing_report_dict)
            self.session.merge(updated_report)
            self.session.commit()
            return ReportSchema.from_orm(updated_report)
        return None

    def delete(self, report_id: int) -> bool:
        report = self.session.get(Report, report_id)
        if report:
            self.session.delete(report)
            self.session.commit()
            return True
        return False