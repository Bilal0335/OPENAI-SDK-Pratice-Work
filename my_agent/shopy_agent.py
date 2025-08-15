from agents import Agent
from my_config.gemini_config import GEMINI_MODEL
from my_tool.fun_tool import shopping_tool

shopping_agents_tool = Agent (
    name="shopping_agents_tool ",
    instructions="You are a shopping assistant who can help users to find products and its details using API",
    model=GEMINI_MODEL,
    tools=[shopping_tool]
)