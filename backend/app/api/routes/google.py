from fastapi import APIRouter, Request , Depends
from fastapi.responses import RedirectResponse
from app.services.google_service import oauth
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.health_metric import HealthMetric
from datetime import date
from app.models.user import User
from app.core.dependencies import get_current_user
from app.services.google_fit_service import fetch_google_fit_steps


router = APIRouter()

@router.get("/connect")
async def google_connect(request: Request):

    redirect_uri = "http://localhost:8000/google/callback"

    return await oauth.google.authorize_redirect(request, redirect_uri)

@router.get("/callback")
async def google_callback(request: Request, db: Session = Depends(get_db)):

    token = await oauth.google.authorize_access_token(request)

    userinfo = token.get("userinfo")
    email = userinfo["email"]

    user = db.query(User).filter(User.email == email).first()

    if not user:
        return {"error": "User not found"}

    user.google_access_token = token["access_token"]
    user.google_refresh_token = token.get("refresh_token")
    user.google_connected = True

    db.commit()

    return {"message": "Google Fit connected successfully"}

@router.post("/sync")
def sync_google_fit(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    access_token = current_user.google_access_token

    data = fetch_google_fit_steps(access_token)

    steps = 0

    try:
        buckets = data["bucket"]

        for bucket in buckets:
            datasets = bucket["dataset"]

            for dataset in datasets:
                points = dataset["point"]

                for point in points:
                    value = point["value"][0]["intVal"]
                    steps += value

    except Exception:
        return {"error": "Unable to parse Google Fit data"}

    metric = HealthMetric(
        steps=steps,
        date=date.today(),
        source="google_fit",
        user_id=current_user.id
    )

    db.add(metric)
    db.commit()

    return {
        "message": "Google Fit data synced",
        "steps": steps
    }