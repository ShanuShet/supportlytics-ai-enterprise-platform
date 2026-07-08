from datetime import datetime


class ReportGenerator:

    def __init__(self, analytics):

        self.analytics = analytics

    def generate(self):

        return {

            "generated_at": datetime.now().isoformat(),

            "report": self.analytics.generate_dashboard()

        }