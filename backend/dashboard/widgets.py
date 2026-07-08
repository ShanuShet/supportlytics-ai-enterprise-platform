class DashboardWidgets:
    """
    Dashboard widget configuration.
    """

    @staticmethod
    def available_widgets():

        return [

            {
                "title": "Total Tickets",
                "icon": "ticket"
            },

            {
                "title": "Resolved Tickets",
                "icon": "check"
            },

            {
                "title": "Pending Approvals",
                "icon": "clock"
            },

            {
                "title": "Security Alerts",
                "icon": "shield"
            },

            {
                "title": "AI Predictions",
                "icon": "brain"
            },

            {
                "title": "Traffic Simulator",
                "icon": "activity"
            }

        ]