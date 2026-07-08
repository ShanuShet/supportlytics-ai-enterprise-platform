from typing import Dict, Any
from .base_agent import BaseAgent


class ResolutionAgent(BaseAgent):

    def __init__(self):
        super().__init__("Resolution Agent")

    async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:

        category = context["category"]

        if category == "Network & Infrastructure":

            return {
                "status": "RESOLVED",
                "risk_score": 0.15
            }

        return {
            "status": "PENDING_REVIEW",
            "risk_score": 0.45
        }