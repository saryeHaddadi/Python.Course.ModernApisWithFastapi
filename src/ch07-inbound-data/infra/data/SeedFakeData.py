import asyncio
from web.viewmodels.Location import Location
from core.entities.ReportSubmitted import ReportSubmitted
from app.services.ReportService import AddReport

def seed_fake_data():
    pass
    # loc = Location(city='Portland', state='OR', country='US')
    # asyncio.run(AddReport(ReportSubmitted(description="Misty sunrise today, beautifuul!", location=loc)))
    # asyncio.run(AddReport(ReportSubmitted(description="Clouds over downtown", location=loc)))



