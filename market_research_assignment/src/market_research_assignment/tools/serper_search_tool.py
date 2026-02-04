from crewai_tools import SerperDevTool

# Initialize only the SerperDevTool with your specific parameters
search_tool = SerperDevTool(
    country="ca",
    locale="en-CA",
    location="Halifax, Nova Scotia, Canada",
    n_results=2,
)
