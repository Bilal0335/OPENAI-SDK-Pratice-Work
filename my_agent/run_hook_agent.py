

# ! run_hook.py
from agents import Agent
from my_config.gemini_config import GEMINI_MODEL
from my_config.groq_config import GROQ_MODEL
from my_hook.my_agent_hook import MyAgentHook
from my_tool.fun_tool import add


math_assistant= Agent(
    name="math_assistant",
    instructions="You are a helpful math_assistant.",
    handoff_description="This is a good math teacher",
    model=GEMINI_MODEL,
    hooks=MyAgentHook(),
    tools=[add]
)

hook_run_ag= Agent(
    name="Hook_Run_Agent",
    instructions="You are a helpful assistant.",
    hooks=MyAgentHook(),
    model=GEMINI_MODEL,
    handoffs=[math_assistant]
)
