from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String

from backend.database.base import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)

    ticket_id = Column(String, unique=True, index=True, nullable=False)

    title = Column(String, nullable=False)

    description = Column(String, nullable=False)

    category = Column(String)

    priority = Column(String)

    status = Column(String)

    assigned_team = Column(String)

    user_name = Column(String)

    department = Column(String)

    country = Column(String)

    risk_score = Column(Float, default=0.0)

    created_at = Column(DateTime, default=datetime.utcnow)

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )