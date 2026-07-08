from backend.database.base import Base
from backend.database.database import engine

# Import every model
from backend.models.ticket import Ticket
from backend.models.user import User
from backend.models.analytics import Analytics
from backend.models.prediction import Prediction
from backend.models.approval import Approval


def initialize_database():
    Base.metadata.create_all(bind=engine)