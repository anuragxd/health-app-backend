from sqlalchemy.orm import Session
from datetime import date, timedelta

from app.models.health_metric import HealthMetric
from app.models.goal import Goal

def get_last_week_metrics(db: Session, user_id: int):

    today = date.today()
    week_ago = today - timedelta(days=7)

    metrics = db.query(HealthMetric).filter(
        HealthMetric.user_id == user_id,
        HealthMetric.date >= week_ago
    ).all()

    return metrics

def calculate_weight_trend(metrics):

    if len(metrics) < 2:
        return 0

    first_weight = metrics[0].weight
    last_weight = metrics[-1].weight

    return last_weight - first_weight

def calculate_steps_average(metrics):

    if not metrics:
        return 0

    total_steps = sum(m.steps for m in metrics)

    return total_steps / len(metrics)

def calculate_calorie_deficit(metrics, goal):

    if not metrics or not goal:
        return 0

    total_deficit = 0

    for m in metrics:

        deficit = goal.daily_calorie_target - m.calories
        total_deficit += deficit

    return total_deficit

def calculate_progress(metrics, goal):

    if not metrics or not goal:
        return 0

    latest_weight = metrics[-1].weight

    progress = goal.target_weight - latest_weight

    return progress