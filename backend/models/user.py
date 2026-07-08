from sqlalchemy import Column, Integer, String

from backend.database.base import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(String, unique=True)

    full_name = Column(String)

    email = Column(String)

    department = Column(String)

    role = Column(String)

    security_clearance = Column(String)

    mfa_enabled = Column(String)