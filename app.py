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
    goal="Reseaarch, analyze, and synthesize comprehensive information on {topic} from reliable web sources",
    backstory= "You're an expert research analyst with advanced web research skills."
                "You excel at finding, analyzing, and synthesizing information from"
                "across the internet using search tools. You're skilled at"
                "distinguishing reliable sources from unreliable ones,"
                "fact-checking, cross-referencing information, and"
                "identifying key patterns and insights. You provide"
                "well-organized research briefs with proper citations"
                "and source verification. Your analysis includes both"
                "raw data and interpreted insights, making complex"
                "information accessible and actionable.",
    allow_delegation = False,
    verbose = True,
    tools = [search_tool],
    llm = llm


)

