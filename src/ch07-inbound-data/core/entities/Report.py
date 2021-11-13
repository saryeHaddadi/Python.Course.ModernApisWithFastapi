import datetime
from typing import Optional
from core.entities.ReportSubmitted import ReportSubmitted

class Report(ReportSubmitted):
    id: str
    created_date: Optional[datetime.datetime]




