from pydantic import BaseModel
from datetime import date


class HealthMetricCreate(BaseModel):

    weight: float
    steps: int
    sleep: float
    calories: int
    water: float
    date: date


class HealthMetricResponse(BaseModel):

    id: int
    weight: float
    steps: int
    sleep: float
    calories: int
    water: float
    date: date

    class Config:
        from_attributes = True