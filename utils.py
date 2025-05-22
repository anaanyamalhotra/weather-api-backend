
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_coords(location):
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={API_KEY}"
    res = requests.get(geo_url).json()
    if res:
        return res[0]["lat"], res[0]["lon"]
    return None, None

def get_air_quality(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
    res = requests.get(url).json()
    return res["list"][0] if "list" in res else {}

def get_weather_data(location, unit):
    lat, lon = get_coords(location)
    if lat is None:
        return {"error": "Location not found"}
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units={unit}&appid={API_KEY}"
    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units={unit}&appid={API_KEY}"
    weather = requests.get(weather_url).json()
    forecast = requests.get(forecast_url).json()
    aqi = get_air_quality(lat, lon)
    return {
        "weather": weather,
        "forecast": forecast,
        "aqi": aqi,
        "coords": {"lat": lat, "lon": lon}
    }
