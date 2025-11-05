# 📦 Installation Guide for Data Analysis Project

## Python Version Requirement
- **Python >= 3.10 and < 3.14**

## Installation Methods

### Option 1: Using UV (Recommended - matches project setup)
```bash
cd "/Users/michalfischbein/projects/final project flow/the_super_crew"
uv venv
source .venv/bin/activate  # On macOS/Linux
# OR
.venv\Scripts\activate  # On Windows

uv pip install -e .
```

### Option 2: Using pip with requirements.txt
```bash
cd "/Users/michalfischbein/projects/final project flow/the_super_crew"
pip install -r requirements.txt
```

### Option 3: Using pip with pyproject.toml
```bash
cd "/Users/michalfischbein/projects/final project flow/the_super_crew"
pip install -e .
```

## Complete Dependency List

### Core Framework Dependencies
1. **crewai[tools]>=0.201.1,<1.0.0**
   - Main CrewAI framework with tools support
   - Includes: Agent, Crew, Task, Flow classes
   - Includes: crewai_tools package

2. **python-dotenv>=1.0.0**
   - For loading environment variables from `.env` file
   - Used in: main.py, data_analist_crew.py, visualizetion_crew.py

3. **pydantic>=2.0.0**
   - Data validation (used by CrewAI and in main.py for BaseModel)
   - Usually included with crewai but explicitly listed for clarity

### Data Analysis Dependencies
4. **pandas>=2.0.0**
   - Used in: EDA.py, statistical_analisys.py
   - For reading CSV files and data manipulation

5. **numpy>=1.24.0**
   - Used in: EDA.py, statistical_analisys.py
   - For numerical operations and array handling

6. **scipy>=1.10.0**
   - Used in: statistical_analisys.py (optional, has fallback)
   - For statistical functions (zscore)
   - Note: Code has fallback if not installed, but recommended

### Visualization Dependencies
7. **matplotlib>=3.7.0**
   - Used by: visualization crew (viz_executor agent via CodeInterpreterTool)
   - For creating static charts (PNG output)

8. **seaborn>=0.12.0**
   - Used by: visualization crew
   - For statistical visualizations (built on matplotlib)

9. **plotly>=5.14.0**
   - Used by: visualization crew
   - For interactive charts (HTML output)

## Additional Tools Included with crewai[tools]

The following tools are automatically available when installing `crewai[tools]`:
- **SerperDevTool** - Web search (requires SERPER_API_KEY in .env)
- **FileReadTool** - Read file contents
- **CSVSearchTool** - Search CSV files
- **CodeInterpreterTool** - Execute Python code (requires visualization libraries)

## Environment Variables Required

Create a `.env` file in the project root with:

```env
# Required for CrewAI agents
OPENAI_API_KEY=your_openai_api_key_here

# Required for action_advisor agent (web search)
SERPER_API_KEY=your_serper_api_key_here
```

## Verification

After installation, verify your setup:

```bash
python -c "import crewai; import pandas; import numpy; import matplotlib; import seaborn; import plotly; print('✅ All dependencies installed successfully!')"
```

## Summary

**Total packages to install: 9**
- 3 Core framework packages
- 3 Data analysis packages  
- 3 Visualization packages

All dependencies are now listed in both `pyproject.toml` and `requirements.txt` for your convenience.

