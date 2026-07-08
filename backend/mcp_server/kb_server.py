"""
MCP-Based Knowledge Retrieval Server & Tool Definitions for Supportlytics AI.
Exposes standard IT tools for Knowledge Base search, SOP lookup, system health checks, and IAM verification.
"""
from typing import Dict, Any, List

# Mock IT Knowledge Base Articles
KB_ARTICLES = [
    {
        "id": "KB-0101",
        "title": "Resolving Cisco AnyConnect VPN Disconnections on Windows 11",
        "category": "Network & Infrastructure",
        "tags": ["vpn", "windows11", "network", "cisco", "disconnect"],
        "content": "Step 1: Open Device Manager -> Network Adapters -> Cisco AnyConnect Mobility Client.\nStep 2: Disable IPv6 on virtual adapter if using enterprise MTU.\nStep 3: Run 'ipconfig /flushdns' in PowerShell.\nStep 4: Update MTU size to 1300 bytes using command 'netsh interface ipv4 set subinterface \"vnic\" mtu=1300 store=persistent'."
    },
    {
        "id": "KB-0102",
        "title": "Standard Operating Procedure: Elevated Database Access Request",
        "category": "IAM & Access Management",
        "tags": ["database", "postgres", "access", "production", "admin"],
        "content": "SOP-902: All production database write or superuser requests require Human Supervisor Approval (HITL). Temporary tokens may be granted for a maximum duration of 4 hours upon approval by SecOps. Risk Score threshold: 0.85."
    },
    {
        "id": "KB-0103",
        "title": "Printer Queue Spooler Reset Procedure",
        "category": "Hardware & Peripherals",
        "tags": ["printer", "spooler", "hardware"],
        "content": "Stop Print Spooler service ('net stop spooler'), delete contents in 'C:\\Windows\\System32\\spool\\PRINTERS', restart spooler service ('net start spooler')."
    },
    {
        "id": "KB-0104",
        "title": "Outlook / Microsoft 365 Authentication Failure",
        "category": "Software & Applications",
        "tags": ["outlook", "email", "office365", "mfa"],
        "content": "Verify user MFA status in Azure AD portal. Clear cached credentials in Windows Credential Manager under Generic Credentials -> MicrosoftOffice16."
    }
]

SYSTEM_HEALTH = {
    "vpn_gateway": {"status": "HEALTHY", "latency_ms": 14, "load": "42%"},
    "azure_ad_iam": {"status": "HEALTHY", "latency_ms": 8, "load": "18%"},
    "prod_postgres_cluster": {"status": "DEGRADED", "latency_ms": 120, "load": "91%", "note": "High CPU utilization on node-01"},
    "office_365": {"status": "HEALTHY", "latency_ms": 22, "load": "30%"}
}

def search_kb(query: str) -> List[Dict[str, Any]]:
    """Searches the IT Knowledge Base for articles matching keywords in the query."""
    query_lower = query.lower()
    results = []
    for article in KB_ARTICLES:
        match_count = sum(1 for tag in article["tags"] if tag in query_lower)
        if match_count > 0 or any(word in article["title"].lower() for word in query_lower.split()):
            results.append({
                "article_id": article["id"],
                "title": article["title"],
                "category": article["category"],
                "summary": article["content"][:200] + "...",
                "relevance_score": match_count
            })
    if not results:
        # Fallback to default article if no direct keyword match
        results.append({
            "article_id": KB_ARTICLES[0]["id"],
            "title": KB_ARTICLES[0]["title"],
            "category": KB_ARTICLES[0]["category"],
            "summary": KB_ARTICLES[0]["content"][:200] + "...",
            "relevance_score": 1
        })
    return results

def get_sop(sop_id: str) -> Dict[str, Any]:
    """Retrieves standard operating procedure documentation by SOP/Article ID."""
    for article in KB_ARTICLES:
        if article["id"].lower() == sop_id.lower() or sop_id.lower() in article["title"].lower():
            return article
    return {"error": f"SOP or Article with ID '{sop_id}' not found.", "fallback": KB_ARTICLES[1]}

def check_system_status(service_name: str) -> Dict[str, Any]:
    """Retrieves real-time infrastructure and service health metrics."""
    key = service_name.lower().replace(" ", "_")
    for sys_key, data in SYSTEM_HEALTH.items():
        if sys_key in key or key in sys_key:
            return {"service": sys_key, "data": data}
    return {"service": service_name, "data": {"status": "UNKNOWN", "load": "N/A", "note": "Service telemetry unmonitored."}}

def verify_user_access(user_id: str) -> Dict[str, Any]:
    """Queries Active Directory / IAM to verify user credentials and security clearance."""
    return {
        "user_id": user_id,
        "identity_verified": True,
        "mfa_active": True,
        "security_clearance": "TIER-2_SENIOR",
        "current_roles": ["DataAnalyst", "DevOps_Contributor"],
        "is_vip": "vip" in user_id.lower() or "senior" in user_id.lower()
    }

def get_dashboard_metrics():
    """
    Returns dashboard statistics.
    """
    return {
        "total_tickets": 1520,
        "resolved": 1310,
        "pending": 82,
        "blocked": 18,
        "automation_rate": 86.2
    }

def find_similar_tickets(query: str):
    results = search_kb(query)
    return {
        "query": query,
        "similar_incidents": results
    }

def recommend_resolution(ticket_category: str):
    if ticket_category == "Network & Infrastructure":
        return {
            "recommendation":
            "Flush DNS, reset MTU, restart VPN adapter."
        }
    elif ticket_category == "IAM & Access Management":
        return {
            "recommendation":
            "Verify MFA and request supervisor approval."
        }
    return {
        "recommendation":
        "Refer to Standard Troubleshooting Guide."
    }

def historical_statistics():
    return {
        "network_incidents": 420,
        "iam_incidents": 180,
        "software_incidents": 520,
        "hardware_incidents": 400
    }

def predict_priority(category: str):
    if category == "Network & Infrastructure":
        return {
            "prediction": "HIGH",
            "confidence": 0.94
        }
    return {
        "prediction": "MEDIUM",
        "confidence": 0.81
    }

def simulator_status():
    return {
        "running": False,
        "tickets_generated": 0,
        "speed": "Normal"
    }

def ai_agent_health():
    return {
        "triage_agent": "Healthy",
        "knowledge_agent": "Healthy",
        "prediction_agent": "Healthy",
        "resolution_agent": "Healthy"
    }

