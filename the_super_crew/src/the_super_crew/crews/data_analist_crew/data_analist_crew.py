from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool, FileReadTool
from dotenv import load_dotenv
from pathlib import Path

from typing import List

# Load environment variables from .env file
load_dotenv()

# Get workspace root path (where data_cleaned.csv is located)
# data_analist_crew.py is at: the_super_crew/src/the_super_crew/crews/data_analist_crew/data_analist_crew.py
# Going up 6 levels gets us to workspace root
workspace_root = Path(__file__).parent.parent.parent.parent.parent.parent

# Initialize tools
serper_tool = SerperDevTool()
file_read_tool = FileReadTool()

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


@CrewBase
class DataAnalistCrew:
    """Data Analist Crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # If you would like to add tools to your crew, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def data_detective(self) -> Agent:
        return Agent(
            config=self.agents_config["data_detective"],  # type: ignore[index]
            tools=[file_read_tool],  # FileReadTool to read statistical_analysis_report.md
        )

    @agent
    def insight_generator(self) -> Agent:
        return Agent(
            config=self.agents_config["insight_generator"],  # type: ignore[index]
            tools=[file_read_tool],  # FileReadTool to read data_analysis_findings.md
        )

    @agent
    def action_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config["action_advisor"],  # type: ignore[index]
            tools=[serper_tool, file_read_tool],  # Add SerperDevTool and FileReadTool
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def analyze_data_task(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_data_task"],  # type: ignore[index]
        )

    @task
    def generate_insights_task(self) -> Task:
        return Task(
            config=self.tasks_config["generate_insights_task"],  # type: ignore[index]
        )

    @task
    def provide_recommendations_task(self) -> Task:
        return Task(
            config=self.tasks_config["provide_recommendations_task"],  # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Research Crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
