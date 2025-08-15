# from agents import Agent, handoff
# import rich
# from my_config.gemini_config import GEMINI_MODEL
# from my_tool.fun_tool import add
# from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX

# math_agent = Agent(
#     name="math_agent",
#     instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
#     You are a helpful math assistant.
#     Your job is to directly solve math-related questions such as arithmetic,
#     algebra, geometry, trigonometry, calculus, and applied word problems.
#     Always show step-by-step working and give the final answer clearly.
#     """,
#     model=GEMINI_MODEL,
#     tools=[add],
#     handoff_description="This agent handles all math-related questions and calculations."
# )

# english_agent = Agent(
#     name="english_agent",
#     instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
#     You are a helpful English language assistant.
#     Your job is to directly provide answers for any English-related request,
#     such as writing essays, correcting grammar, improving text, translating,
#     summarizing, drafting emails, or explaining concepts in English.
#     Always respond with the full, detailed answer without giving a placeholder message.
#     """,
#     model=GEMINI_MODEL,
#     tools=[add],
#     handoff_description="This agent handles all English-related questions and tasks."
# )

# assistant = Agent(
#     name="assistant",
#     instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
#     You are a helpful general assistant.
#     If the question is about math, hand off to math_agent.
#     If the question is about English, hand off to english_agent.
#     If it’s not related to math or English, handle it yourself and provide the best possible answer.
#     """,
#     model=GEMINI_MODEL,
#     handoffs=[
#         math_agent,
#         english_agent
#     ]
# )


# my_agent/handoff_agent.py

from agents import Agent, handoff
from my_config.gemini_config import GEMINI_MODEL
from my_data_type.data_type import MyhandoffData
from my_service.service_fun import service
from my_tool.fun_tool import add, substract, multiply, weather
from agents.extensions import handoff_filters
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX

from validators.valid_tool import tool_validated

# Math Agent
math_agent = Agent(
    name="math_agent",
    instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
    You are a helpful math assistant.
    Handle math-related questions: arithmetic, algebra, geometry, trigonometry, calculus, 
    and applied math problems. Always show step-by-step working and the final answer.
    """,
    model=GEMINI_MODEL,
    tools=[add, substract, multiply],
    handoff_description="This agent handles math-related questions.",
    
)

# Wrap Math Agent as Handoff Tool
math_teacher = handoff(
    agent=math_agent,
    tool_name_override="transfer_to_math_agent",
    # tool_name_override="math_teacher",
    tool_description_override="This agent handles math questions.",
    on_handoff=service,
    input_type=MyhandoffData,
    input_filter=handoff_filters.remove_all_tools,
    # is_enabled=False
    is_enabled=tool_validated
)

# Main Assistant
assistant = Agent(
    name="assistant",
    instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
    You are a helpful general assistant.
    If the question is about math, hand off to math_agent.
    If it's about weather, use the weather tool.
    If both appear in the same query, handle both and give a combined answer.
    """,
    model=GEMINI_MODEL,
    handoffs=[math_teacher],
    tools=[weather]
)




# ! clone agent 
# from agents import Agent, handoff
# from my_config.gemini_config import GEMINI_MODEL
# from my_data_type.data_type import MyhandoffData
# from my_service.service_fun import service
# from my_tool.fun_tool import add, substract, multiply, weather
# from agents.extensions import handoff_filters
# from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
# from validators.valid_tool import tool_validated

# # -----------------------
# # 1. Math Agent
# # -----------------------
# math_agent = Agent(
#     name="math_agent",
#     instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
#     You are a helpful math assistant.
#     Handle math-related questions: arithmetic, algebra, geometry, trigonometry, calculus, 
#     and applied math problems. Always show step-by-step working and the final answer.
#     """,
#     model=GEMINI_MODEL,
#     tools=[add, substract, multiply],
#     handoff_description="This agent handles math-related questions.",
# )

# # -----------------------
# # 2. Science Agent (Clone from Math Agent)
# # -----------------------
# science_agent = math_agent.clone()
# science_agent.name = "science_agent"
# science_agent.instructions = f"""{RECOMMENDED_PROMPT_PREFIX}
# You are a helpful science assistant.
# Handle science-related questions: physics, chemistry, biology, astronomy, and scientific explanations.
# Always explain step-by-step and give the final answer clearly.
# """
# science_agent.handoff_description = "This agent handles science-related questions."

# # -----------------------
# # 3. Wrap Math Agent as Handoff Tool
# # -----------------------
# math_teacher = handoff(
#     agent=math_agent,
#     tool_name_override="transfer_to_math_agent",
#     tool_description_override="This agent handles math questions.",
#     on_handoff=service,
#     input_type=MyhandoffData,
#     input_filter=handoff_filters.remove_all_tools,
#     is_enabled=tool_validated
# )

# # -----------------------
# # 4. Wrap Science Agent as Handoff Tool
# # -----------------------
# science_teacher = handoff(
#     agent=science_agent,
#     tool_name_override="transfer_to_science_agent",
#     tool_description_override="This agent handles science questions.",
#     on_handoff=service,
#     input_type=MyhandoffData,
#     input_filter=handoff_filters.remove_all_tools,
#     is_enabled=tool_validated
# )

# # -----------------------
# # 5. Main Assistant
# # -----------------------
# assistant = Agent(
#     name="assistant",
#     instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
#     You are a helpful general assistant.
#     If the question is about math, hand off to math_agent.
#     If it's about science, hand off to science_agent.
#     If it's about weather, use the weather tool.
#     If multiple appear in the same query, handle all and give a combined answer.
#     """,
#     model=GEMINI_MODEL,
#     handoffs=[math_teacher, science_teacher],
#     tools=[weather]
# )
