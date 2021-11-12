from web.viewmodels.Location import Location

def get_report(loc: Location, units: str) -> dict:
    q = f'{loc.city},{loc.country},{loc.state}'
    apiKey = '123'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={q}&appid={apiKey}&units={units}'
