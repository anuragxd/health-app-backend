from pydantic import BaseModel


class DietPlanResponse(BaseModel):

    breakfast: str
    lunch: str
    dinner: str
    snacks: str
    total_calories: int