import rich
from my_config.gemini_config import GEMINI_MODEL
from agents import Agent
from my_tool.fun_tool import add,sub,multiply,get_date,get_weather

math_tool_agents = Agent(
    name="math_tool_agents",
    instructions="You are helpfull math_tool_agent.",
    model=GEMINI_MODEL,
    tools=[add,sub,multiply,get_weather,get_date]
)

# rich.print(math_tool_agents.name)
# rich.print(math_tool_agents.tools)