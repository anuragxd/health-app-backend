from fastapi import FastAPI
from app.db.database import engine
from app.db.base import Base
from starlette.middleware.sessions import SessionMiddleware


from app.api.routes import auth ,health , goal, analytics , diet , google

app = FastAPI(title="Health AI Backend")
app.add_middleware(
    SessionMiddleware,
    secret_key="super-secret-session-key"
)

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(health.router, prefix="/health", tags=["health"])
app.include_router(goal.router, prefix="/goal", tags=["goal"])
app.include_router(analytics.router, prefix="/analytics",tags=["analytics"])
app.include_router(
    diet.router,
    prefix="/diet",
    tags=["diet"]
)
app.include_router(
    google.router,
    prefix="/google",
    tags=["google"]
)
@app.get("/")
def root():
    return {"message": "Health AI Backend Running"}