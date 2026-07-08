from sqlalchemy.orm import Session

from backend.models.ticket import Ticket


class TicketRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Ticket).all()

    def get_by_ticket_id(self, ticket_id: str):
        return (
            self.db.query(Ticket)
            .filter(Ticket.ticket_id == ticket_id)
            .first()
        )

    def create(self, ticket: Ticket):

        self.db.add(ticket)
        self.db.commit()
        self.db.refresh(ticket)

        return ticket

    def update(self, ticket: Ticket):

        self.db.commit()
        self.db.refresh(ticket)

        return ticket

    def delete(self, ticket: Ticket):

        self.db.delete(ticket)
        self.db.commit()