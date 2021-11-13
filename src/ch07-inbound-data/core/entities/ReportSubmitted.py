from pydantic import BaseModel
from web.viewmodels.Location import Location

class ReportSubmitted(BaseModel):
    description: str
    location: Location

