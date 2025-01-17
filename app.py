from crewai import Agents, Task, Crew , LLM
from crewai_tools import SerperDevTool


from dotenv import load_dotenv                         

load_dotenv()


topic = "Medical Industry using Generative AI"


# Tool 1 
llm = LLM(model='gpt-4')


# Tool 2 

search_tool = SerperDevTool(n=10)


# Agent 1d

senior_research_analyst = Agent(
    role="Senior Research Analyst",
    goal
)

