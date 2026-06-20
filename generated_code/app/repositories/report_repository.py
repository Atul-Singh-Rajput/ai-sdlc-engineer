from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import report
from app.schemas import report as schema

class ReportRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_reports(self):
        query = select(report.Report)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_report_by_id(self, report_id: int):
        query = select(report.Report).where(report.Report.id == report_id)
        result = await self.session.execute(query)
        return result.scalar()

    async def create_report(self, report_schema: schema.ReportCreate):
        new_report = report.Report(**report_schema.dict())
        self.session.add(new_report)
        await self.session.commit()
        await self.session.refresh(new_report)
        return new_report

    async def update_report(self, report_id: int, report_schema: schema.ReportUpdate):
        query = select(report.Report).where(report.Report.id == report_id)
        result = await self.session.execute(query)
        existing_report = result.scalar()
        if existing_report:
            existing_report.title = report_schema.title
            existing_report.description = report_schema.description
            self.session.add(existing_report)
            await self.session.commit()
            await self.session.refresh(existing_report)
            return existing_report
        return None

    async def delete_report(self, report_id: int):
        query = select(report.Report).where(report.Report.id == report_id)
        result = await self.session.execute(query)
        existing_report = result.scalar()
        if existing_report:
            await self.session.delete(existing_report)
            await self.session.commit()
            return True
        return False