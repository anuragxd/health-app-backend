from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.user import User
from app.models.goal import Goal
from app.schema.analytics_schema import ProgressResponse
from app.core.dependencies import get_current_user

from app.services.analytics_service import (
    get_last_week_metrics,
    calculate_weight_trend,
    calculate_steps_average,
    calculate_calorie_deficit,
    calculate_progress
)

router = APIRouter()

@router.get("/progress", response_model=ProgressResponse)
def get_progress(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    metrics = get_last_week_metrics(db, current_user.id)

    goal = db.query(Goal).filter(
        Goal.user_id == current_user.id
    ).order_by(Goal.start_date.desc()).first()

    weight_trend = calculate_weight_trend(metrics)

    steps_avg = calculate_steps_average(metrics)

    deficit = calculate_calorie_deficit(metrics, goal)

    progress = calculate_progress(metrics, goal)

    return {
        "weight_trend": weight_trend,
        "weekly_steps_average": steps_avg,
        "calorie_deficit": deficit,
        "weekly_progress": progress
    }