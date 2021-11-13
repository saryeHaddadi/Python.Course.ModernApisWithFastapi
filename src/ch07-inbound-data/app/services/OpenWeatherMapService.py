from typing import Optional, Tuple
from core.entities.Temperature import Temperature
from web.viewmodels.Location import Location
from infra.cache import weather_cache
from infra.exceptions.ValidationException import ValidationException
import requests
import httpx


apiKey: Optional[str] = None

def get_report(loc: Location, units: str) -> Temperature:
    q, url = build_query_and_url(loc, units)

    resp = requests.get(url)
    resp.raise_for_status()
    return extract_temperature(resp)

async def get_report_async(loc: Location, units: str) -> Temperature:
    loc, units = clean_and_validate_params(loc, units)
    
    forecast = weather_cache.get_weather(loc, units)
    if forecast is not None:
        return forecast
    
    q, url = build_query_and_url(loc, units)

    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        if resp.status_code != 200:
            raise ValidationException(resp.text, resp.status_code)
    
    forecast = extract_temperature(resp)
    weather_cache.set_weather(loc, units, forecast)
    return forecast

def extract_temperature(resp: requests.Response):
    return Temperature(**resp.json()['main'])


def build_query_and_url(loc: Location, units: str):
    q = f'{loc.city},{loc.country},{loc.state}' if loc.state is not None else f'{loc.city},{loc.country}'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={q}&appid={apiKey}&units={units}'
    
    return (q, url)


def clean_and_validate_params(loc: Location, units: str) -> Tuple[Location, str]:
    loc.city = loc.city.lower().strip()
    if not loc.country:
        loc.country = "us"
    else:
        loc.country = loc.country.lower().strip()

    if len(loc.country) != 2:
        error = f"Invalid country: {loc.country}. It must be a two letter abbreviation such as US or GB."
        raise ValidationException(status_code=400, error_msg=error)

    if loc.state:
        loc.state = loc.state.strip().lower()

    if loc.state and len(loc.state) != 2:
        error = f"Invalid state: {loc.state}. It must be a two letter abbreviation such as CA or KS (use for US only)."
        raise ValidationException(status_code=400, error_msg=error)

    if units:
        units = units.strip().lower()

    valid_units = {'standard', 'metric', 'imperial'}
    if units not in valid_units:
        error = f"Invalid units '{units}', it must be one of {valid_units}."
        raise ValidationException(status_code=400, error_msg=error)

    return loc, units




