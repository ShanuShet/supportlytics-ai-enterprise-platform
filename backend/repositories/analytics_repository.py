from sqlalchemy import func
from sqlalchemy.orm import Session

from backend.models.ticket import Ticket


class AnalyticsRepository:

    def __init__(self, db: Session):
        self.db = db

    def overview(self):

        total = self.db.query(Ticket).count()

        resolved = (
            self.db.query(Ticket)
            .filter(func.lower(Ticket.status) == "resolved")
            .count()
        )

        open_tickets = (
            self.db.query(Ticket)
            .filter(func.lower(Ticket.status) == "open")
            .count()
        )

        in_progress = (
            self.db.query(Ticket)
            .filter(func.lower(Ticket.status) == "in_progress")
            .count()
        )

        pending = (
            self.db.query(Ticket)
            .filter(func.lower(Ticket.status) == "pending")
            .count()
        )

        blocked = (
            self.db.query(Ticket)
            .filter(func.lower(Ticket.status) == "blocked_security_violation")
            .count()
        )

        return {

            "totalTicketsProcessed": total,

            "autoResolved": resolved,

            "openTickets": open_tickets,

            "hitlHolds": in_progress + pending,

            "inProgress": in_progress,

            "pendingTickets": pending,

            "blockedThreats": blocked,

            "resolutionRate":
                round((resolved / total) * 100, 1)
                if total else 0

        }

    def category_distribution(self):

        data = (
            self.db.query(
                Ticket.category,
                func.count(Ticket.id)
            )
            .group_by(Ticket.category)
            .all()
        )

        return [

            {

                "category": row[0],

                "count": row[1]

            }

            for row in data

        ]

    def priority_distribution(self):

        data = (
            self.db.query(
                Ticket.priority,
                func.count(Ticket.id)
            )
            .group_by(Ticket.priority)
            .all()
        )

        return [

            {

                "priority": row[0],

                "count": row[1]

            }

            for row in data

        ]

    def country_distribution(self):

        data = (
            self.db.query(
                Ticket.country,
                func.count(Ticket.id)
            )
            .group_by(Ticket.country)
            .all()
        )

        return [

            {

                "country": row[0],

                "count": row[1]

            }

            for row in data

        ]