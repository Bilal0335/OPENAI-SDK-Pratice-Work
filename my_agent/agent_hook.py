# ! agent_hook.py
from agents import Agent
from my_config.gemini_config import GEMINI_MODEL
from my_hook.my_agent_hook import MyAgentHook
from my_tool.fun_tool import add

# math_assistant = Agent(
#     name="Hook_Agent_Math",
#     instructions="You are a helpful math assistant.",
#     model=GEMINI_MODEL,
#     hooks=MyAgentHook(),
#     tools=[add]
# )

hook_agent = Agent(
    name="Hook_Agent_Main",
    instructions="You are a helpful assistant.",
    model=GEMINI_MODEL,
    hooks=MyAgentHook(),
    # handoffs=[math_assistant]
)
