from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base


class Goal(Base):

    __tablename__ = "goals"

    id = Column(Integer, primary_key=True, index=True)

    goal_type = Column(String)
    target_weight = Column(Float)
    daily_calorie_target = Column(Integer)

    start_date = Column(Date)

    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User")