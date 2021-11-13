import json
from typing import Optional
from web.viewmodels.Location import Location
import requests
import httpx

apiKey: Optional[str] = None

def get_report(loc: Location, units: str) -> dict:
    q, url = build_query_and_url(loc, units)

    resp = requests.get(url)
    resp.raise_for_status()
    return extract_temperature(resp)

async def get_report_async(loc: Location, units: str) -> dict:
    q, url = build_query_and_url(loc, units)

    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()
    return extract_temperature(resp)

def extract_temperature(resp: requests.Response):
    return resp.json()['main']

def build_query_and_url(loc: Location, units: str):
    q = f'{loc.city},{loc.country},{loc.state}' if loc.state is not None else f'{loc.city},{loc.country}'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={q}&appid={apiKey}&units={units}'
    
    return (q, url)
