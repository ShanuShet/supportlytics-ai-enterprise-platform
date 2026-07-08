from backend.mcp_server.kb_server import SYSTEM_HEALTH


def check_system_status(service_name: str) -> Dict[str, Any]:
    """Retrieves real-time infrastructure and service health metrics."""
    key = service_name.lower().replace(" ", "_")
    for sys_key, data in SYSTEM_HEALTH.items():
        if sys_key in key or key in sys_key:
            return {"service": sys_key, "data": data}
    return {"service": service_name, "data": {"status": "UNKNOWN", "load": "N/A", "note": "Service telemetry unmonitored."}}
