from sqlalchemy import Column, Integer, String, Float

from backend.database.base import Base


class Approval(Base):

    __tablename__ = "approvals"

    id = Column(Integer, primary_key=True)

    ticket_id = Column(String)

    action = Column(String)

    reviewer = Column(String)

    comments = Column(String)

    status = Column(String)

    risk_score = Column(Float)