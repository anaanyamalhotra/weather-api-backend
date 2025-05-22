from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from models import Base, WeatherRecord, engine, SessionLocal
from schemas import WeatherCreate, WeatherUpdate
import crud
from utils import get_weather_data

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/weather")
def get_weather(location: str = Query(...), unit: str = Query("metric")):
    try:
        return get_weather_data(location, unit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch weather: {str(e)}")

@app.post("/records/")
def create_record(record: WeatherCreate):
    db: Session = SessionLocal()
    return crud.create_weather_record(db, record)

@app.get("/records/")
def read_records():
    db: Session = SessionLocal()
    return crud.get_all_records(db)

@app.put("/records/{record_id}")
def update_record(record_id: int, updated: WeatherUpdate):
    db: Session = SessionLocal()
    return crud.update_weather_record(db, record_id, updated)

@app.delete("/records/{record_id}")
def delete_record(record_id: int):
    db: Session = SessionLocal()
    return crud.delete_weather_record(db, record_id)