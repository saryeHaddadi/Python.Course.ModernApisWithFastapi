from pydantic import BaseModel
from decimal import Decimal

class Temperature(BaseModel):
    temp: Decimal
    feels_like: Decimal
    temp_min: Decimal
    temp_max: Decimal
    pressure: Decimal
    humidity: Decimal

