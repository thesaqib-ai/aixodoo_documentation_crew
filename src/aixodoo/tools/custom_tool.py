from crewai_tools import BaseTool


class MyCustomTool(BaseTool):
    name: str = "Odoo Studio 17 Documentations"
    description: str = (
        "Call this tool for any query related to Odoo Studio implementation."
    )

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."
