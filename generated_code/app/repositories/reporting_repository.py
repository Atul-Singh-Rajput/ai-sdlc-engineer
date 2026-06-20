from sqlalchemy import select
from sqlalchemy.orm import Session
from generated_code.app.models.reporting import Reporting
from generated_code.app.schemas.reporting import Reporting as ReportingSchema
from typing import List, Optional

class ReportingRepository:
    def get_all(self, db: Session) -> List[ReportingSchema]:
        return db.query(Reporting).all()

    def get_by_id(self, db: Session, id: int) -> Optional[ReportingSchema]:
        return db.query(Reporting).filter(Reporting.id == id).first()

    def create(self, db: Session, reporting: ReportingSchema) -> ReportingSchema:
        db_report = Reporting(**reporting.dict())
        db.add(db_report)
        db.commit()
        db.refresh(db_report)
        return db_report

    def update(self, db: Session, id: int, reporting: ReportingSchema) -> Optional[ReportingSchema]:
        db_report = db.query(Reporting).filter(Reporting.id == id).first()
        if db_report:
            db_report.data = reporting.data
            db.commit()
            db.refresh(db_report)
            return db_report
        return None

    def delete(self, db: Session, id: int) -> bool:
        db_report = db.query(Reporting).filter(Reporting.id == id).first()
        if db_report:
            db.delete(db_report)
            db.commit()
            return True
        return False