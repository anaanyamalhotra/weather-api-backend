
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from utils import get_weather_data

app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/weather")
def weather(location: str = Query(...), unit: str = Query("metric")):
    return get_weather_data(location, unit)
