import fastapi
from typing import Optional
from fastapi import Depends
from app.services.WeatherService import GetWeatherValue
from web.viewmodels.Location import Location

router = fastapi.APIRouter()


@router.get('/api/weather/{city}')
def GetWeather(loc: Location = Depends(),
               units: Optional[str] = 'metric'):
    return GetWeatherValue(loc, units)





