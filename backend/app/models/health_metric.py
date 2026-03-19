from sqlalchemy import Column, Integer, Float, Date, ForeignKey, String, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.base import Base


class HealthMetric(Base):

    __tablename__ = "health_metrics"
    __table_args__ = (
        UniqueConstraint("user_id", "date", name="unique_user_day"),
    )

    id = Column(Integer, primary_key=True, index=True)

    weight = Column(Float)
    steps = Column(Integer)
    sleep = Column(Float)
    calories = Column(Integer)
    water = Column(Float)

    date = Column(Date)

    source = Column(String, default="manual")

    created_at = Column(DateTime, default=datetime.utcnow)

    user_id = Column(Integer, ForeignKey("users.id"))