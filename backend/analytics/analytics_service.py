from .kpi_engine import KPIEngine
from .trend_analysis import TrendAnalysis
from .dashboard_metrics import DashboardMetrics


class AnalyticsService:
    """
    Central Analytics Service
    """

    def __init__(self, tickets):

        self.tickets = tickets

        self.kpi = KPIEngine(tickets)
        self.trends = TrendAnalysis(tickets)
        self.dashboard = DashboardMetrics(tickets)

    def generate_dashboard(self):

        return {

            "overview": self.dashboard.overview(),

            "kpis": self.kpi.calculate(),

            "category_distribution": self.trends.category_distribution(),

            "priority_distribution": self.trends.priority_distribution(),

            "country_distribution": self.trends.country_distribution(),

            "daily_trend": self.trends.daily_ticket_trend()

        }