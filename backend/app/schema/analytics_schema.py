from pydantic import BaseModel


class ProgressResponse(BaseModel):

    weight_trend: float
    weekly_steps_average: float
    calorie_deficit: float
    weekly_progress: float