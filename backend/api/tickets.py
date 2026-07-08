from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database.session import get_db
from backend.schemas.ticket_schema import TicketCreate
from backend.services.ticket_service import TicketService

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)


@router.get("/")
def get_all_tickets(db: Session = Depends(get_db)):
    service = TicketService(db)
    return service.get_all_tickets()


@router.get("/{ticket_id}")
def get_ticket(ticket_id: str, db: Session = Depends(get_db)):

    service = TicketService(db)

    ticket = service.get_ticket(ticket_id)

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return ticket


@router.post("/")
def create_ticket(
    ticket: TicketCreate,
    db: Session = Depends(get_db)
):
    service = TicketService(db)

    return service.create_ticket(ticket)


@router.put("/{ticket_id}")
def update_ticket(
    ticket_id: str,
    ticket: TicketCreate,
    db: Session = Depends(get_db)
):
    service = TicketService(db)

    updated = service.update_ticket(ticket_id, ticket)

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return updated


@router.delete("/{ticket_id}")
def delete_ticket(
    ticket_id: str,
    db: Session = Depends(get_db)
):

    service = TicketService(db)

    deleted = service.delete_ticket(ticket_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return {
        "message": "Ticket deleted successfully"
    }