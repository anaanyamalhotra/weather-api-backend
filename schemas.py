
from pydantic import BaseModel
from typing import Optional

class WeatherCreate(BaseModel):
    location: str
    temperature: float
    humidity: float
    wind: float
    aqi: int

class WeatherUpdate(BaseModel):
    temperature: Optional[float] = None
    humidity: Optional[float] = None
    wind: Optional[float] = None
    aqi: Optional[int] = None
