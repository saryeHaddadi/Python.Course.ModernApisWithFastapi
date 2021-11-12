from typing import Optional
from pydantic import BaseModel

class Location(BaseModel):
    city: str
    country: str = 'US'
    state: Optional[str] = None
