from backend.mcp_server.kb_server import *

TOOLS = {
    "search_kb": search_kb,
    "get_sop": get_sop,
    "check_system_status": check_system_status,
    "verify_user_access": verify_user_access,
    "dashboard_metrics": get_dashboard_metrics,
    "similar_tickets": find_similar_tickets,
    "recommend_resolution": recommend_resolution,
    "historical_statistics": historical_statistics,
    "predict_priority": predict_priority,
    "simulator_status": simulator_status,
    "ai_agent_health": ai_agent_health
}