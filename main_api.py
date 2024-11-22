from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# MySQL Database setup
DATABASE_URL = "mysql+mysqlconnector://user:test123@localhost/request_db"  # Change as per your MySQL setup

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative class definitions
Base = declarative_base()

# SQLAlchemy Model to store the count
class RequestCount(Base):
    __tablename__ = "request_count"
    id = Column(Integer, primary_key=True, index=True)
    count = Column(Integer, default=0)

# Pydantic Model for response (CountResponse)
class CountResponse(BaseModel):
    count: int

    class Config:
        orm_mode = True  # Tells Pydantic to treat SQLAlchemy models as dicts

# FastAPI app
app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create the database tables (if they don't already exist)
Base.metadata.create_all(bind=engine)

@app.get("/count", response_model=CountResponse)
def get_and_increment_request_count(db: Session = Depends(get_db)):
    # Get the count record from the database
    count_record = db.query(RequestCount).first()

    # If the count record doesn't exist, create it
    if not count_record:
        count_record = RequestCount(count=0)
        db.add(count_record)
        db.commit()
        db.refresh(count_record)

    # Increment the count every time the route is accessed
    count_record.count += 1
    db.commit()  # Commit the increment to the database
    db.refresh(count_record)  # Refresh to get the updated count

    # Return the updated count
    return {"count": count_record.count}
