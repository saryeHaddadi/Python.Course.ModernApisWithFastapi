import fastapi
from typing import Optional
from fastapi import Depends
from app.services.WeatherService import GetWeatherValue, GetWeatherValueAsync
from web.viewmodels.Location import Location
from infra.exceptions.ValidationException import ValidationException

router = fastapi.APIRouter()


@router.get('/api/weather/{city}')
async def GetWeatherAsync(loc: Location = Depends(), units: Optional[str] = 'metric'):
    try:
        return await GetWeatherValueAsync(loc, units)
    except ValidationException as e:
        return fastapi.Response(content= e.error_msg, status_code= e.status_code)
    except Exception as e:
        print(f"Server crashed while processing request: {e}")
        return fastapi.Response(content="Error processing your request.", status_code=500)
        




