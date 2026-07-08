from typing import Dict, Any
from .base_agent import BaseAgent
from backend.security.guardrails import evaluate_ticket_security


class SecurityAgent(BaseAgent):

    def __init__(self):
        super().__init__("Security Agent")

    async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:

        return evaluate_ticket_security(
            context["title"],
            context["description"]
        )