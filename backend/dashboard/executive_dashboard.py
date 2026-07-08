class ExecutiveDashboard:
    """
    Executive level dashboard cards.
    """

    def __init__(self, tickets):
        self.tickets = tickets

    def summary(self):

        total = len(self.tickets)

        resolved = len(
            [
                t
                for t in self.tickets
                if t.get("status") == "RESOLVED"
            ]
        )

        pending = len(
            [
                t
                for t in self.tickets
                if t.get("status") == "PENDING_APPROVAL"
            ]
        )

        blocked = len(
            [
                t
                for t in self.tickets
                if t.get("status") == "BLOCKED_SECURITY_VIOLATION"
            ]
        )

        return {
            "total_tickets": total,
            "resolved_tickets": resolved,
            "pending_approvals": pending,
            "security_blocks": blocked,
        }