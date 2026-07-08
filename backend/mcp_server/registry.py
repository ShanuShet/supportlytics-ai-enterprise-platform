from backend.mcp_server.tools import TOOLS


class MCPRegistry:

    @staticmethod
    def list_tools():

        return list(TOOLS.keys())

    @staticmethod
    def execute(tool_name, *args, **kwargs):

        if tool_name not in TOOLS:

            raise ValueError("Unknown MCP Tool")

        return TOOLS[tool_name](*args, **kwargs)