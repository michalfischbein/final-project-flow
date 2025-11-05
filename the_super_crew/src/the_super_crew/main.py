#!/usr/bin/env python

import os
import subprocess
import sys
from pathlib import Path

# Add src directory to path if running as script (not as module)
# This allows imports to work both ways: `python main.py` and `python -m the_super_crew.main`
# Check if we're running as a script (not imported as a module)
if __name__ == "__main__" or not __package__:
    src_dir = Path(__file__).parent.parent
    if str(src_dir) not in sys.path:
        sys.path.insert(0, str(src_dir))

from dotenv import load_dotenv
from pydantic import BaseModel

from crewai.flow import Flow, listen, start

# Load environment variables from .env file
load_dotenv()

from the_super_crew.crews.data_analist_crew.data_analist_crew import DataAnalistCrew
from the_super_crew.crews.visualization_crew.visualizetion_crew import VisualizationCrew


class DataAnalysisState(BaseModel):
    eda_complete: bool = False
    statistical_analysis_complete: bool = False
    analysis_complete: bool = False
    findings: str = ""
    visualization_complete: bool = False


class DataAnalysisFlow(Flow[DataAnalysisState]):

    @start()
    def run_eda(self):
        """Run EDA.py to clean and prepare the data"""
        print("=" * 80)
        print("🚀 Starting EDA (Exploratory Data Analysis)")
        print("=" * 80)
        
        # Get the path to EDA.py and workspace root
        # main.py is at: the_super_crew/src/the_super_crew/main.py
        # Going up 4 levels gets us to workspace root
        workspace_root = Path(__file__).parent.parent.parent.parent
        eda_path = workspace_root / "the_super_crew" / "src" / "the_super_crew" / "crews" / "data_analist_crew" / "data_analist_codes" / "EDA.py"
        
        # Change to workspace root directory for scripts that read CSV files
        original_cwd = Path.cwd()
        try:
            os.chdir(workspace_root)
            result = subprocess.run(
                [sys.executable, str(eda_path)],
                capture_output=True,
                text=True,
                check=False
            )
            if result.returncode != 0:
                print("❌ Error output from EDA.py:")
                print(result.stderr)
                if result.stdout:
                    print("Standard output:")
                    print(result.stdout)
                raise Exception(f"EDA.py failed with return code {result.returncode}\nError: {result.stderr}")
            # Print stdout if there's output
            if result.stdout:
                print(result.stdout)
            print("✅ EDA completed successfully")
            self.state.eda_complete = True
        finally:
            os.chdir(original_cwd)

    @listen(run_eda)
    def run_statistical_analysis(self):
        """Run statistical_analisys.py to generate statistical report"""
        print("=" * 80)
        print("📊 Starting Statistical Analysis")
        print("=" * 80)
        
        # Get the path to statistical_analisys.py and workspace root
        # main.py is at: the_super_crew/src/the_super_crew/main.py
        # Going up 4 levels gets us to workspace root
        workspace_root = Path(__file__).parent.parent.parent.parent
        stats_path = workspace_root / "the_super_crew" / "src" / "the_super_crew" / "crews" / "data_analist_crew" / "data_analist_codes" / "statistical_analisys.py"
        
        # Change to workspace root directory for scripts that read CSV files
        original_cwd = Path.cwd()
        try:
            os.chdir(workspace_root)
            result = subprocess.run(
                [sys.executable, str(stats_path)],
                capture_output=True,
                text=True,
                check=False
            )
            if result.returncode != 0:
                print("❌ Error output from statistical_analisys.py:")
                print(result.stderr)
                if result.stdout:
                    print("Standard output:")
                    print(result.stdout)
                raise Exception(f"statistical_analisys.py failed with return code {result.returncode}\nError: {result.stderr}")
            # Print stdout if there's output
            if result.stdout:
                print(result.stdout)
            print("✅ Statistical analysis completed successfully")
            self.state.statistical_analysis_complete = True
        finally:
            os.chdir(original_cwd)

    @listen(run_statistical_analysis)
    def run_data_analysis(self):
        """Run the CrewAI data analysis crew"""
        print("=" * 80)
        print("🤖 Starting CrewAI Data Analysis")
        print("=" * 80)
        
        result = (
            DataAnalistCrew()
            .crew()
            .kickoff()
        )

        print("Data analysis complete", result.raw)
        self.state.findings = result.raw
        self.state.analysis_complete = True

    @listen(run_data_analysis)
    def run_visualization(self):
        """Run the CrewAI visualization crew"""
        print("=" * 80)
        print("📊 Starting CrewAI Visualization")
        print("=" * 80)
        
        result = (
            VisualizationCrew()
            .crew()
            .kickoff()
        )

        print("Visualization complete", result.raw)
        self.state.visualization_complete = True


def kickoff():
    data_analysis_flow = DataAnalysisFlow()
    data_analysis_flow.kickoff()


def plot():
    data_analysis_flow = DataAnalysisFlow()
    data_analysis_flow.plot()


if __name__ == "__main__":
    kickoff()
