from sqlalchemy import Column, Integer, String, Float

from backend.database.base import Base


class Analytics(Base):

    __tablename__ = "analytics"

    id = Column(Integer, primary_key=True)

    metric = Column(String)

    value = Column(Float)

    category = Column(String)

    recorded_at = Column(String)