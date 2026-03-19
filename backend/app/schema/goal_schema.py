from pydantic import BaseModel
from datetime import date


class GoalCreate(BaseModel):

    goal_type: str
    target_weight: float
    daily_calorie_target: int
    start_date: date


class GoalResponse(BaseModel):

    id: int
    goal_type: str
    target_weight: float
    daily_calorie_target: int
    start_date: date

    class Config:
        from_attributes = True