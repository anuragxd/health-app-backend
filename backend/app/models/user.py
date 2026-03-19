from sqlalchemy import Column, Integer, String, Boolean
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    password_hash = Column(String)
    age = Column(Integer)
    height = Column(Integer)
    google_access_token = Column(String, nullable=True)

    google_refresh_token = Column(String, nullable=True)

    google_connected = Column(Boolean, default=False)