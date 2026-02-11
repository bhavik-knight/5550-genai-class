from pathlib import Path
from crewai import Agent, Task, Crew, Process, LLM
from crewai.project import CrewBase, agent, crew, task
from .tools.serper_search_tool import search_tool
import os
from dotenv import load_dotenv

@CrewBase
class MarketResearchAssignment:
    """MarketResearchAssignment crew for strategic analysis"""

    # These paths are relative to the file when using @CrewBase
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    load_dotenv()

    def __init__(self):
        # Initialize the LLM
        self.llm = LLM(
            model=os.getenv("MODEL"),
            temperature=0.1
        )
        self.output_dir = Path("output")
        self._ensure_output_directory()

    def _ensure_output_directory(self):
        """Creates the output folder if it doesn't exist."""
        if not self.output_dir.exists():
            self.output_dir.mkdir(parents=True, exist_ok=True)

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            tools=[search_tool],
            llm=self.llm,
            max_iter=1,
            allow_delegation=False,
            verbose=True
        )

    @agent
    def analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['analyst'],
            llm=self.llm,
            max_iter=1,
            allow_delegation=False,
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
        )

    @task
    def analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['analysis_task'],
            context=[self.research_task()],
            # Note: The filename is dynamically set in main.py or interpolated if using placeholders
        )

    @crew
    def crew(self) -> Crew:
        """Creates the MarketResearchAssignment crew"""
        return Crew(
            agents=self.agents, # Automatically created by @agent
            tasks=self.tasks,   # Automatically created by @task
            process=Process.sequential,
            verbose=True,
        )
