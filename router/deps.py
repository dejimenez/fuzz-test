from typing import Generator
from database.database import SessionLocal, engine

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()