from sqlalchemy import Column, Integer, String, Float, DateTime, Text, JSON
from sqlalchemy.sql import func
from backend.database import Base

class Event(Base):
    __tablename__ = "events"
    
    id = Column(Integer, primary_key=True, index=True)
    image = Column(String(1000))  
    name = Column(String(255), index=True, nullable=False)
    genre = Column(String(100), index=True)  
    date = Column(String(50), nullable=False)  
    location = Column(String(500))  
    organizer = Column(String(255))  
    rating = Column(Float, default=5.0)  
    reviews = Column(JSON, default=list)  
    description = Column(Text)  
    ticket = Column(String(1000))  
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())