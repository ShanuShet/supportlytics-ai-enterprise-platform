from typing import Dict, Any
from .base_agent import BaseAgent
from backend.mcp_server.kb_server import search_kb


class KnowledgeAgent(BaseAgent):

    def __init__(self):
        super().__init__("Knowledge Agent")

    async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:

        query = context["title"] + " " + context["description"]

        articles = search_kb(query)

        return {
            "kb_articles": articles
        }