from backend.analytics.analytics_service import AnalyticsService


def dashboard_data(tickets):

    analytics = AnalyticsService(tickets)

    return analytics.generate_dashboard()