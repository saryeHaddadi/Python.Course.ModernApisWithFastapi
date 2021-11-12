import fastapi
from app.services.WeatherService import GetWeatherValue

router = fastapi.APIRouter()

@router.get('/api/weather')
def GetWeather():
    return GetWeatherValue()
