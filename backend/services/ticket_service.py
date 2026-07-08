from sqlalchemy.orm import Session
from backend.utils.helpers import generate_ticket_id
from backend.models.ticket import Ticket
from backend.repositories.ticket_repository import TicketRepository


class TicketService:

    def __init__(self, db: Session):
        self.repository = TicketRepository(db)

    def get_all_tickets(self):
        return self.repository.get_all()

    def get_ticket(self, ticket_id: str):
        return self.repository.get_by_ticket_id(ticket_id)

    def create_ticket(self, ticket_data):

        ticket = Ticket(
            **ticket_data.dict(),
            ticket_id=generate_ticket_id(),
            status="PROCESSING",
            risk_score=0.0
        )

        return self.repository.create(ticket)

    def update_ticket(self, ticket_id, updated_ticket):

        ticket = self.repository.get_by_ticket_id(ticket_id)

        if not ticket:
            return None

        for key, value in updated_ticket.dict().items():
            setattr(ticket, key, value)

        return self.repository.update(ticket)

    def delete_ticket(self, ticket_id):

        ticket = self.repository.get_by_ticket_id(ticket_id)

        if not ticket:
            return False

        self.repository.delete(ticket)

        return True