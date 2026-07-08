from pydantic import BaseModel
from typing import Optional


class TicketCreate(BaseModel):
    title: str
    description: str
    category: str
    priority: str
    user_name: str
    department: str
    country: str
    assigned_team: Optional[str] = None


class TicketUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    priority: Optional[str] = None
    status: Optional[str] = None
    assigned_team: Optional[str] = None


class TicketResponse(BaseModel):

    ticket_id: str

    title: str

    description: str

    category: str

    priority: str

    status: str

    assigned_team: Optional[str]

    user_name: str

    department: str

    country: str

    risk_score: float

    class Config:
        from_attributes = True