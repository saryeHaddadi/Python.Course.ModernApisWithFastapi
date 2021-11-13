import fastapi
from typing import Optional
from fastapi import Depends
from app.services.WeatherService import GetWeatherValue, GetWeatherValueAsync
from web.viewmodels.Location import Location

router = fastapi.APIRouter()


@router.get('/api/weather/{city}')
async def GetWeatherAsync(loc: Location = Depends(),
               units: Optional[str] = 'metric'):
    return await GetWeatherValueAsync(loc, units)





