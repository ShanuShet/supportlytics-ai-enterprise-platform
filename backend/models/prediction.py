from sqlalchemy import Column, Integer, String, Float

from backend.database.base import Base


class Prediction(Base):

    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True)

    ticket_id = Column(String)

    predicted_priority = Column(String)

    predicted_category = Column(String)

    predicted_resolution_time = Column(Float)

    predicted_sla = Column(String)

    confidence = Column(Float)