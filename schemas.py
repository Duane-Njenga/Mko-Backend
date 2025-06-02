from pydantic import BaseModel, Field, validator
from typing import Optional, List, Any
from datetime import datetime

class EventBase(BaseModel):
    image: Optional[str] = Field(None, max_length=1000, description="Event image URL")
    name: str = Field(..., min_length=1, max_length=255, description="Event name")
    genre: Optional[str] = Field(None, max_length=100, description="Event genre")
    date: str = Field(..., description="Event date (YYYY-MM-DD format)")
    location: Optional[str] = Field(None, max_length=500, description="Event location")
    organizer: Optional[str] = Field(None, max_length=255, description="Event organizer")
    rating: Optional[float] = Field(5.0, ge=0, le=5, description="Event rating")
    reviews: Optional[List[Any]] = Field(default_factory=list, description="Event reviews")
    description: Optional[str] = Field(None, description="Event description")
    ticket: Optional[str] = Field(None, max_length=1000, description="Ticket purchase URL")

    @validator('rating')
    def validate_rating(cls, v):
        if v is not None and (v < 0 or v > 5):
            raise ValueError('Rating must be between 0 and 5')
        return v

    @validator('date')
    def validate_date_format(cls, v):
        try:
            datetime.strptime(v, '%Y-%m-%d')
        except ValueError:
            raise ValueError('Date must be in YYYY-MM-DD format')
        return v

class EventCreate(EventBase):
    pass

class EventUpdate(BaseModel):
    image: Optional[str] = Field(None, max_length=1000)
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    genre: Optional[str] = Field(None, max_length=100)
    date: Optional[str] = Field(None)
    location: Optional[str] = Field(None, max_length=500)
    organizer: Optional[str] = Field(None, max_length=255)
    rating: Optional[float] = Field(None, ge=0, le=5)
    reviews: Optional[List[Any]] = Field(None)
    description: Optional[str] = Field(None)
    ticket: Optional[str] = Field(None, max_length=1000)

    @validator('rating')
    def validate_rating(cls, v):
        if v is not None and (v < 0 or v > 5):
            raise ValueError('Rating must be between 0 and 5')
        return v

    @validator('date')
    def validate_date_format(cls, v):
        if v is not None:
            try:
                datetime.strptime(v, '%Y-%m-%d')
            except ValueError:
                raise ValueError('Date must be in YYYY-MM-DD format')
        return v

class EventResponse(EventBase):
    id: int

    class Config:
        from_attributes = True