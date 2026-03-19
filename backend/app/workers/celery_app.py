from celery import Celery

celery_app = Celery(
    "health_worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

celery_app.conf.beat_schedule = {
    "sync-google-fit-every-6-hours": {
        "task": "app.workers.health_tasks.sync_google_fit_data",
        "schedule": 21600
    }
}

celery_app.conf.timezone = "UTC"