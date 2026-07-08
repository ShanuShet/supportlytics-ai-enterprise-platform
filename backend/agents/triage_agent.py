from typing import Dict, Any
from .base_agent import BaseAgent


class TriageAgent(BaseAgent):

    def __init__(self):
        super().__init__("Triage Agent")

    async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:

        title = context["title"].lower()
        description = context["description"].lower()

        text = f"{title} {description}"

        if any(word in text for word in ["vpn", "wifi", "network", "dns"]):

            return {
                "category": "Network & Infrastructure",
                "priority": "HIGH",
                "assigned_team": "Network Operations"
            }

        elif any(word in text for word in ["password", "admin", "login"]):

            return {
                "category": "IAM & Access Management",
                "priority": "HIGH",
                "assigned_team": "Security Team"
            }

        return {
            "category": "Software & Applications",
            "priority": "MEDIUM",
            "assigned_team": "Application Support"
        }