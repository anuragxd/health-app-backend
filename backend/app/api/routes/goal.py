from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.goal import Goal
from app.models.user import User
from app.schema.goal_schema import GoalCreate, GoalResponse
from app.core.dependencies import get_current_user

router = APIRouter()

@router.post("/set", response_model=GoalResponse)
def set_goal(
    data: GoalCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    goal = Goal(
        goal_type=data.goal_type,
        target_weight=data.target_weight,
        daily_calorie_target=data.daily_calorie_target,
        start_date=data.start_date,
        user_id=current_user.id
    )

    db.add(goal)
    db.commit()
    db.refresh(goal)

    return goal

@router.get("/current", response_model=GoalResponse | None)
def get_current_goal(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    goal = db.query(Goal).filter(
        Goal.user_id == current_user.id
    ).order_by(Goal.start_date.desc()).first()

    return goal