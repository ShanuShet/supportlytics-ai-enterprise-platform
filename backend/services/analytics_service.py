from sqlalchemy.orm import Session

from backend.repositories.analytics_repository import AnalyticsRepository


class AnalyticsService:

    def __init__(self, db: Session):

        self.repository = AnalyticsRepository(db)

    def overview(self):

        return self.repository.overview()

    def categories(self):

        return self.repository.category_distribution()

    def priorities(self):

        return self.repository.priority_distribution()

    def countries(self):

        return self.repository.country_distribution()