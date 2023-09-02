# Copyright 2023 Marin Pejcin


from app.database.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
