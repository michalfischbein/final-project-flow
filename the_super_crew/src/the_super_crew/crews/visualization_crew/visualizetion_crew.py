from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import FileReadTool, CSVSearchTool
from dotenv import load_dotenv
from pathlib import Path

from typing import List

# Load environment variables from .env file
load_dotenv()

# Get workspace root path (where data_cleaned.csv is located)
# visualizetion_crew.py is at: the_super_crew/src/the_super_crew/crews/visualization_crew/visualizetion_crew.py
# Going up 6 levels gets us to workspace root
workspace_root = Path(__file__).parent.parent.parent.parent.parent.parent
csv_file_path = workspace_root / "data_cleaned.csv"

# Initialize tools (lazy initialization for CSVSearchTool to avoid API calls at import time)
file_read_tool = FileReadTool()
# CSVSearchTool is initialized lazily in the agent method to avoid API calls during import

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class VisualizationCrew:
    """Visualization Crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def viz_planner(self) -> Agent:
        return Agent(
            config=self.agents_config["viz_planner"],  # type: ignore[index]
            tools=[file_read_tool],  # Add FileReadTool to read action_recommendations.md and business_insights.md
        )

    @agent
    def viz_code_generator(self) -> Agent:
        # Initialize CSVSearchTool lazily to avoid API calls at import time
        csv_search_tool = CSVSearchTool(csv=str(csv_file_path))
        return Agent(
            config=self.agents_config["viz_code_generator"],  # type: ignore[index]
            tools=[file_read_tool, csv_search_tool],  # Add tools for code generator
        )

    @agent
    def viz_executor(self) -> Agent:
        return Agent(
            config=self.agents_config["viz_executor"],
            tools=[file_read_tool],  # FileReadTool to read visualization_code.md and create generate_charts.py script
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def define_visuals_task(self) -> Task:
        return Task(
            config=self.tasks_config["define_visuals_task"],  # type: ignore[index]
        )

    @task
    def generate_viz_code_task(self) -> Task:
        return Task(
            config=self.tasks_config["generate_viz_code_task"],  # type: ignore[index]
        )

    @task
    def execute_visualizations_task(self) -> Task:
        return Task(
            config=self.tasks_config["execute_visualizations_task"],  # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Visualization Crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
