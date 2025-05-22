
from sqlalchemy.orm import Session
from models import WeatherRecord
from schemas import WeatherCreate, WeatherUpdate

def create_weather_record(db: Session, record: WeatherCreate):
    db_record = WeatherRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

def get_all_records(db: Session):
    return db.query(WeatherRecord).all()

def update_weather_record(db: Session, record_id: int, record: WeatherUpdate):
    db_record = db.query(WeatherRecord).filter(WeatherRecord.id == record_id).first()
    if not db_record:
        return {"error": "Record not found"}
    for key, value in record.dict(exclude_unset=True).items():
        setattr(db_record, key, value)
    db.commit()
    return db_record

def delete_weather_record(db: Session, record_id: int):
    db_record = db.query(WeatherRecord).filter(WeatherRecord.id == record_id).first()
    if not db_record:
        return {"error": "Record not found"}
    db.delete(db_record)
    db.commit()
    return {"deleted": record_id}
