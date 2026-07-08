class KPIEngine:

    def __init__(self, tickets):

        self.tickets = tickets

    def calculate(self):

        total = len(self.tickets)

        resolved = len([
            t for t in self.tickets
            if t.get("status") == "RESOLVED"
        ])

        automation_rate = round(
            (resolved / total) * 100,
            2
        ) if total else 0

        average_risk = round(

            sum(
                t.get("risk_score", 0)
                for t in self.tickets
            ) / total,

            2

        ) if total else 0

        return {

            "total_tickets": total,

            "automation_rate": automation_rate,

            "average_risk_score": average_risk

        }