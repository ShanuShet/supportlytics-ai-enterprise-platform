from datetime import datetime


class RealtimeMetrics:
    """
    Live dashboard metrics.
    """

    def __init__(self, tickets):
        self.tickets = tickets

    def metrics(self):

        processing = len(
            [
                t
                for t in self.tickets
                if t.get("status") == "PROCESSING"
            ]
        )

        return {
            "current_time": datetime.now().isoformat(),
            "processing_tickets": processing,
            "active_agents": 5,
            "simulator_status": "Stopped",
            "system_health": "Healthy"
        }