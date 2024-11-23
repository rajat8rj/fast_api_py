from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os

DATABASE_URL = os.getenv("DATABASE_URL","mysql+mysqlconnector://user:test123@localhost/request_db")


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class RequestCount(Base):
    __tablename__ = "request_count"
    id = Column(Integer, primary_key=True, index=True)
    count = Column(Integer, default=0)

class CountResponse(BaseModel):
    count: int

    class Config:
        orm_mode = True

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)

@app.get("/count", response_model=CountResponse)
def get_and_increment_request_count(db: Session = Depends(get_db)):

    count_record = db.query(RequestCount).first()

    if not count_record:
        count_record = RequestCount(count=0)
        db.add(count_record)
        db.commit()
        db.refresh(count_record)


    count_record.count += 1
    db.commit()
    db.refresh(count_record)

    return {"count": count_record.count}
