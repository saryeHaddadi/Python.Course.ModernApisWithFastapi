import fastapi
from typing import List
from app.services import ReportService
from infra.exceptions.ValidationException import ValidationException
from core.entities.Report import Report
from core.entities.ReportSubmitted import ReportSubmitted

router = fastapi.APIRouter()

@router.get('/api/reports', name='reports', response_model=List[Report])
async def GetReports() -> List[Report]:
    try:
        return await ReportService.GetReports()
    except ValidationException as e:
        return fastapi.Response(content= e.error_msg, status_code= e.status_code)
    except Exception as e:
        print(f"Server crashed while processing request: {e}")
        return fastapi.Response(content="Error processing your request.", status_code=500)
        
@router.post('/api/reports', name='reports', response_model=Report, status_code=201)
async def AddReport(reportSubmitted: ReportSubmitted) -> Report:
    try:
        return await ReportService.AddReport(reportSubmitted)
    except ValidationException as e:
        return fastapi.Response(content= e.error_msg, status_code= e.status_code)
    except Exception as e:
        print(f"Server crashed while processing request: {e}")
        return fastapi.Response(content="Error processing your request.", status_code=500)
     

