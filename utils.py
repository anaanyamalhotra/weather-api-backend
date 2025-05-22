
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
    if "list" in res and res["list"]:
        data = res["list"][0]
        aqi = data.get("main", {}).get("aqi")
        components = data.get("components", {})
        if aqi is not None:
            return {
                "aqi": aqi,  # ✅ FLATTENED structure
                "components": components
            }
    return {} 

def get_weather_data(location, unit):
    coords, err = get_coords(location)
    if err or not coords:
        raise HTTPException(status_code=404, detail="Location not found.")

    lat, lon = coords["lat"], coords["lon"]
    u = "metric" if unit == "metric" else "imperial"

    try:
        weather = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units={u}&appid={API_KEY}"
        ).json()

        forecast = requests.get(
            f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units={u}&appid={API_KEY}"
        ).json()

        aqi = get_air_quality(lat, lon)

        return {
            "weather": weather,
            "forecast": forecast,
            "coords": coords,
            "aqi": aqi  # Always dict (already flattened earlier)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Weather fetch failed: {str(e)}
