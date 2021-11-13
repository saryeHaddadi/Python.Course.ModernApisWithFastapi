import datetime
from sortedcontainers import SortedKeyList
from typing import List
from core.entities.Report import Report
from core.entities.ReportSubmitted import ReportSubmitted
import uuid

__reports: SortedKeyList[Report] = SortedKeyList([], lambda x : x.created_date)

async def GetReports() -> List[Report]:
    # Would be an async call here
    return list(__reports)

async def AddReport(reportSubmitted: ReportSubmitted) -> Report:
    report = Report(id= str(uuid.uuid4()),
                    description= reportSubmitted.description,
                    location = reportSubmitted.location,
                    created_date=datetime.datetime.now())
    # Simulate saving to the DB
    # Would be an async call here
    __reports.add(report)
    return report






