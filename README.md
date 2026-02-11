# Market Research Assignment

This project utilizes CrewAI to perform market research tasks. Follow the instructions below to set up the environment and execute the assignment.

## Setup and Execution

1.  **Install Dependencies**
    
    Run the following command in the root directory to sync dependencies and set up the environment:

    ```bash
    uv sync
    ```

    > **Note:** This command creates a virtual environment. Make sure to activate it (e.g., `source .venv/bin/activate`) or use `uv run` for subsequent commands.

2.  **Navigate to Assignment Folder**

    Change your directory to the `market_research_assignment` folder:

    ```bash
    cd market_research_assignment
    ```

3.  **Run the Crew**

    Execute the crew using the `crewai` command:

    ```bash
    crewai run
    ```

## Output

The execution will generate a markdown file containing the research results. You can find this file in the `output` folder within the `market_research_assignment` directory.
