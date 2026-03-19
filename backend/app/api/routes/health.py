from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date

from app.db.session import get_db
from app.models.health_metric import HealthMetric
from app.schema.health_schema import HealthMetricCreate, HealthMetricResponse
from app.core.dependencies import get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/log", response_model=HealthMetricResponse)
def log_health_metric(
    data: HealthMetricCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    metric = HealthMetric(
        weight=data.weight,
        steps=data.steps,
        sleep=data.sleep,
        calories=data.calories,
        water=data.water,
        date=data.date,
        user_id=current_user.id
    )

    db.add(metric)
    db.commit()
    db.refresh(metric)

    return metric

@router.get("/history", response_model=list[HealthMetricResponse])
def get_history(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    metrics = db.query(HealthMetric).filter(
        HealthMetric.user_id == current_user.id
    ).all()

    return metrics

@router.get("/today", response_model=HealthMetricResponse | None)
def get_today_metrics(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    today = date.today()

    metric = db.query(HealthMetric).filter(
        HealthMetric.user_id == current_user.id,
        HealthMetric.date == today
    ).first()

    return metric