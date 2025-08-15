

# ! run_hook.py
from agents import Agent
from my_config.gemini_config import GEMINI_MODEL
from my_tool.fun_tool import add


hook_run_ag= Agent(
    name="Hook_Run_Agent",
    instructions="You are a helpful assistant.",
    model=GEMINI_MODEL,
)
