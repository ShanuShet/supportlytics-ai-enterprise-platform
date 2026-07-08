from sqlalchemy.orm import Session

from backend.services.analytics_service import AnalyticsService


class DashboardService:

    def __init__(self, db: Session):
        self.analytics = AnalyticsService(db)

    def get_dashboard(self):
        return {
            "overview": self.analytics.overview(),
            "categories": self.analytics.categories(),
            "priorities": self.analytics.priorities(),
            "countries": self.analytics.countries()
        }