"""
Supportlytics AI Database Models

Contains SQLAlchemy models used across the application.
"""

from .ticket import Ticket
from .user import User
from .prediction import Prediction
from .approval import Approval
from .analytics import Analytics

__all__ = [
    "Ticket",
    "User",
    "Prediction",
    "Approval",
    "Analytics"
]