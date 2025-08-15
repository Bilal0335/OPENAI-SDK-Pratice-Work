

# ! session_man.py
from agents import Agent
from my_config.gemini_config import GEMINI_MODEL

sess_agents = Agent(
    name="sess_agents",
    instructions="You are a helpful assistant",
    model=GEMINI_MODEL
)

