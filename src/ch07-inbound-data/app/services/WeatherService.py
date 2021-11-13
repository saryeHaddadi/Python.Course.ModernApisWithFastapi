from core.entities.Temperature import Temperature
from web.viewmodels.Location import Location
from app.services import OpenWeatherMapService

# TODO: revoir la reference du model
def GetWeatherValue(loc: Location, units: str) -> Temperature:
    temp = OpenWeatherMapService.get_report(loc, units)
    return temp

async def GetWeatherValueAsync(loc: Location, units: str) -> Temperature:
    temp = await OpenWeatherMapService.get_report_async(loc, units)
    return temp
