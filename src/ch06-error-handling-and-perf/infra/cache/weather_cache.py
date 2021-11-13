import datetime
from typing import Optional, Tuple
from web.viewmodels.Location import Location

__cache = {}
lifetime_in_hours = 1.0

TIME = 'time'
VALUE = 'value'

def get_weather(loc: Location, units: str) -> Optional[dict]:
    key = __get_key(loc, units)
    data : dict = __cache.get(key)
    if data is None:
        return None
    
    last = data[TIME]
    dt = datetime.datetime.now() - last
    
    if dt / datetime.timedelta(minutes=60) < lifetime_in_hours:
        return data[VALUE]
    else:
        del __cache[key]
        return None
    
def set_weather(loc: Location, units: str, value: dict):
    key = __get_key(loc, units)
    data = __build_payload(value)
    __cache[key] = data
    # __clean_out_of_date()

def __build_payload(value: str):
    return {
        'time': datetime.datetime.now(),
        'value': value
    }

def __get_key(loc: Location, units: str) -> Tuple[str, str, str, str]:
    if (loc.city is None) or (loc.country is None) or (units is None):
        raise Exception("City, country, and units are required")

    return clean_parameters(loc, units)

def clean_parameters(loc: Location, units: str) -> Tuple[str, str, str, str]:
    city = clean_string(loc.city)
    state = clean_string(replace_null_by_empty(loc.state))
    country = clean_string(loc.country)
    units = clean_string(units)

    return city, state, country, units    

def clean_string(string: str) -> str:
    return string.strip().lower()

def replace_null_by_empty(string: str) -> str:
    return ("" if string is None else string)





