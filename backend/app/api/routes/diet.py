from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.user import User
from app.models.goal import Goal
from app.models.health_metric import HealthMetric

from app.core.dependencies import get_current_user
from app.agent.diet_agent import generate_diet_plan
router = APIRouter()

@router.post("/generate")
def generate_plan(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    goal = db.query(Goal).filter(
        Goal.user_id == current_user.id
    ).order_by(Goal.start_date.desc()).first()

    metric = db.query(HealthMetric).filter(
        HealthMetric.user_id == current_user.id
    ).order_by(HealthMetric.date.desc()).first()

    data = {
        "goal": goal.goal_type,
        "current_weight": metric.weight,
        "target_weight": goal.target_weight,
        "daily_calorie_target": goal.daily_calorie_target,
        "steps_avg": metric.steps
    }

    diet_plan = generate_diet_plan(data)

    return {
        "diet_plan": diet_plan
    }