import random

from sqlalchemy.orm import Session

from backend.models.ticket import Ticket


class SimulatorService:

    def __init__(self, db: Session):

        self.db = db

    def generate_tickets(
        self,
        count=10
    ):

        categories = [

            "hardware",
            "software",
            "network",
            "access",
            "other"

        ]

        priorities = [

            "low",
            "medium",
            "high",
            "critical"

        ]

        statuses = [

            "open",
            "in_progress",
            "resolved"

        ]

        locations = [

            "HQ",
            "LAB",
            "Remote"

        ]

        created = []

        current = self.db.query(
            Ticket
        ).count()

        for i in range(count):

            number = current + i + 1

            priority = random.choice(
                priorities
            )

            risk = {

                "critical":0.95,
                "high":0.80,
                "medium":0.55,
                "low":0.25

            }[priority]

            ticket = Ticket(

                ticket_id=f"SIM-{number:05d}",

                title=f"Generated Ticket {number}",

                description="Created by Traffic Simulator",

                category=random.choice(categories),

                priority=priority,

                status=random.choice(statuses),

                assigned_team="AI Team",

                user_name="Simulator",

                department="IT",

                country=random.choice(locations),

                risk_score=risk

            )

            self.db.add(ticket)

            created.append(
                ticket.ticket_id
            )

        self.db.commit()

        return {

            "status":"Simulator Started",

            "generated":len(created),

            "tickets":created

        }