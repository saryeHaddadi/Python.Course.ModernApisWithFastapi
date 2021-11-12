from web.viewmodels.Location import Location
from app.services import OpenWeatherMapService

# TODO: revoir la reference du model
def GetWeatherValue(loc: Location, units: str):
    repport = OpenWeatherMapService.get_report(loc, units)
    return repport


