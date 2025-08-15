from agents import Agent
from my_config.gemini_config import GEMINI_MODEL
from my_tool.my_tools import get_age
from my_instruction.role_base_instruction import role_based_instruction
from my_data_type.data_type import UserData

role_agent = Agent[UserData](
    name="role_agent",
    instructions=role_based_instruction,
    tools=[get_age],
    model=GEMINI_MODEL,
    # tool_use_behavior="run_llm_again"
)

