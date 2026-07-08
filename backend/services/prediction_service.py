from sqlalchemy.orm import Session

from backend.repositories.prediction_repository import PredictionRepository


class PredictionService:

    def __init__(self, db: Session):

        self.repository = PredictionRepository(db)

    def get_ticket(self, ticket_id: str):

        return self.repository.get_ticket(ticket_id)

    def predict_priority(self, ticket_id: str):

        ticket = self.get_ticket(ticket_id)

        if not ticket:
            return None

        priority = (ticket.priority or "MEDIUM").upper()

        confidence = {
            "CRITICAL": 0.98,
            "HIGH": 0.94,
            "MEDIUM": 0.87,
            "LOW": 0.81
        }.get(priority, 0.75)

        return {

            "ticket_id": ticket.ticket_id,

            "predicted_priority": priority,

            "confidence": confidence

        }

    def predict_risk(self, ticket_id: str):

        ticket = self.get_ticket(ticket_id)

        if not ticket:
            return None

        priority = (ticket.priority or "").lower()

        risk_score = ticket.risk_score or 0.0

        if risk_score == 0:

            if priority == "critical":
                risk_score = 0.95

            elif priority == "high":
                risk_score = 0.80

            elif priority == "medium":
                risk_score = 0.55

            elif priority == "low":
                risk_score = 0.25

            else:
                risk_score = 0.10

        if risk_score >= 0.90:
            level = "CRITICAL"

        elif risk_score >= 0.70:
            level = "HIGH"

        elif risk_score >= 0.40:
            level = "MEDIUM"

        else:
            level = "LOW"

        return {

            "ticket_id": ticket.ticket_id,

            "risk_score": round(risk_score, 2),

            "risk_level": level

        }

    def predict_sla(self, ticket_id: str):

        ticket = self.get_ticket(ticket_id)

        if not ticket:
            return None

        priority = (ticket.priority or "").lower()

        sla = {
            "critical": "2 Hours",
            "high": "8 Hours",
            "medium": "24 Hours",
            "low": "48 Hours"
        }.get(priority, "72 Hours")

        return {

            "ticket_id": ticket.ticket_id,

            "predicted_sla": sla

        }

    def predict_resolution(self, ticket_id: str):

        ticket = self.get_ticket(ticket_id)

        if not ticket:
            return None

        priority = (ticket.priority or "").lower()

        hours = {
            "critical": 3,
            "high": 8,
            "medium": 24,
            "low": 48
        }.get(priority, 72)

        return {

            "ticket_id": ticket.ticket_id,

            "predicted_resolution_time": hours,

            "unit": "Hours"

        }

    def predict_all(self, ticket_id: str):

        ticket = self.get_ticket(ticket_id)

        if not ticket:
            return None

        priority = self.predict_priority(ticket_id)
        risk = self.predict_risk(ticket_id)
        sla = self.predict_sla(ticket_id)
        resolution = self.predict_resolution(ticket_id)

        recommendation = self.get_recommendation(
            priority["predicted_priority"]
        )

        return {

            "priority": priority,

            "risk": risk,

            "sla": sla,

            "resolution": resolution,

            "recommendation": recommendation

        }

    def get_recommendation(self, priority):

        recommendations = {

            "CRITICAL":
                "Escalate immediately to the Security Team. Notify management and begin incident response.",

            "HIGH":
                "Assign to the appropriate support team within the next hour.",

            "MEDIUM":
                "Schedule resolution during the current working shift.",

            "LOW":
                "Queue for normal processing according to SLA."

        }

        return recommendations.get(
            priority,
            "No recommendation available."
        )