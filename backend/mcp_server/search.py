
from backend.mcp_server.kb_server import KB_ARTICLES


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