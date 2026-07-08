from sqlalchemy.orm import Session

from backend.models.ticket import Ticket


class PredictionRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_ticket(self, ticket_id: str):

        return (
            self.db.query(Ticket)
            .filter(Ticket.ticket_id == ticket_id)
            .first()
        )

    def get_priority(self, ticket_id: str):

        ticket = self.get_ticket(ticket_id)

        if not ticket:
            return None

        return ticket.priority

    def get_risk_score(self, ticket_id: str):

        ticket = self.get_ticket(ticket_id)

        if not ticket:
            return None

        return ticket.risk_score

    def get_status(self, ticket_id: str):

        ticket = self.get_ticket(ticket_id)

        if not ticket:
            return None

        return ticket.status

    def get_category(self, ticket_id: str):

        ticket = self.get_ticket(ticket_id)

        if not ticket:
            return None

        return ticket.category

    def get_country(self, ticket_id: str):

        ticket = self.get_ticket(ticket_id)

        if not ticket:
            return None

        return ticket.country

    def update_risk_score(
        self,
        ticket_id: str,
        risk_score: float
    ):

        ticket = self.get_ticket(ticket_id)

        if not ticket:
            return None

        ticket.risk_score = risk_score

        self.db.commit()

        self.db.refresh(ticket)

        return ticket