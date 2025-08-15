
# ! tracing_agent.py
from agents import Agent
from my_config.gemini_config import GEMINI_MODEL
from my_config.groq_config import GROQ_MODEL
from my_tool.fun_tool import add


trace_agent = Agent(
    name="trace_agent",
    instructions="You are a helpful assistant",
    tools=[add],
    model=GROQ_MODEL
)

