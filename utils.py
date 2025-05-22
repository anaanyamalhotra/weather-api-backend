import requests
from fastapi import HTTPException
from config import API_KEY

def get_coords(location):
    if "," in location and location.split(",")[0].strip().isdigit():
        zip_code, country_code = location.split(",", 1)
        zip_url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip_code.strip()},{country_code.strip()}&appid={API_KEY}"
        res = requests.get(zip_url)
        if res.status_code == 200:
            data = res.json()
            return {"lat": data["coord"]["lat"], "lon": data["coord"]["lon"]}, None
        else:
            return None, "Invalid ZIP or country code."

    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={API_KEY}"
    geo_res = requests.get(geo_url).json()
    if geo_res:
        return {"lat": geo_res[0]["lat"], "lon": geo_res[0]["lon"]}, None
    return None, "Location not found."

def get_air_quality(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
    res = requests.get(url).json()
    if "list" in res and res["list"]:
        data = res["list"][0]
        aqi = data.get("main", {}).get("aqi")
        components = data.get("components", {})
        if aqi is not None:
            return {
                "aqi": aqi,
                "components": components
            }
    return {"aqi": 0, "components": {}}

def get_weather_data(location, unit):
    coords, err = get_coords(location)
    if err or not coords:
        raise HTTPException(status_code=404, detail="Location not found.")

    lat, lon = coords["lat"], coords["lon"]
    u = "metric" if unit == "metric" else "imperial"

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
        "aqi": aqi
    }
