
# ! my_agent/translate_as_tool_agent.py

from agents import Agent,ModelSettings
import rich
from my_config.groq_config import GROQ_MODEL
from my_tool.fun_tool import add,substract

# ! custom FunctionTool

math_agent = Agent(
    name="math_agent",
    instructions=(
        "You are a helpful math assistant. "
    ),
    tools=[add, substract],
    model=GROQ_MODEL
)

# rich.print(math_agent.tools)
# for s in math_agent.tools:
    # print(s.params_json_schema)


# ! Controlling tool use behavior and tool choice 
# from my_tool.fun_tool import add,sub,multiply
# from agents.agent import StopAtTools

# math_agent = Agent(
#     name="math_agent",
#     instructions=" You are helpfull math_agent assistant. ",
#     tools=[add,sub,multiply],
#     # tool_use_behavior="run_llm_again",
#     # tool_use_behavior="stop_on_first_tool",
#     tool_use_behavior=StopAtTools(stop_at_tool_names=["add","multiply"]),
#     # model_settings=ModelSettings(tool_choice="auto"),
#     # model_settings=ModelSettings(tool_choice="none"),
#     # model_settings=ModelSettings(tool_choice="required"),
#     # model_settings=ModelSettings(tool_choice="sub"),
#     model_settings=ModelSettings(tool_choice="sub",parallel_tool_calls=False),
#     reset_tool_choice=False,
#     model=GROQ_MODEL
# )

# math_agent = Agent(
#     name="math_agent",
#     instructions=(
#         "You are a helpful math assistant. "
#         "When given math instructions, break them down step-by-step and call the appropriate tool "
#         "with JSON arguments like {\"n1\": x, \"n2\": y}."
#     ),
#     tools=[add, sub, multiply],

#     # Important: run_llm_again se agent ek turn me multiple tools call kar sakta hai sequentially.
#     tool_use_behavior="run_llm_again",

#     # Model settings me tool_choice auto rakho taake agent apne hisaab se tool choose kar sake.
#     model_settings=ModelSettings(tool_choice="auto", parallel_tool_calls=False),

#     # Reset tool choice after each turn, taake har nayi input ya turn pe nayi tool select ho sake.
#     reset_tool_choice=False,

#     model=GROQ_MODEL,
# )


# ! reset_tool_choice -->
# Agar False ho to pehli baar tool select kar ke wahi use karta rahe. 
# Agar True ho to har nayi input me dobara tool choose kare.

# reset_tool_choice=False ka matlab kya hai?
# Jab agent multiple tools (jaise add, sub, multiply) ke paas hota hai, to tool choice ka matlab hota hai ki AI model ko kaun sa tool use karna chahiye agle input ke liye.

# Agar reset_tool_choice=True hoga, to agent har turn (ya har user input ke baad) apni tool choice ko reset kar deta hai, yani model har nayi input pe phir se decide karega kaun sa tool use karna hai.

# Agar reset_tool_choice=False hoga (jo tum ne use kiya hai), to agent ek baar tool choose karne ke baad us tool choice ko "yaad" rakhta hai aur agle turns me wahi tool use karta rahega jab tak explicitly change na ho.









# ! pratice work
# ! as_tool

# from my_tool.fun_tool import spanish_agent,french_agent
# orchestrator_agent = Agent(
#     name="orchestrator_agent",
#     instructions=(
#         "You are a translation agent. You use the tools given to you to translate."
#         "If asked for multiple translations, you call the relevant tools."
#     ),
#     tools=[
#         spanish_agent.as_tool(
#             tool_name="translate_to_spanish",
#             tool_description="Translate the user's message to Spanish",
#         ),
#         french_agent.as_tool(
#             tool_name="translate_to_french",
#             tool_description="Translate the user's message to French",
#         ),
#     ],
#     model=GEMINI_MODEL
# )

# rich.print(agent.as_tool)
# rich.print(agent.name)

# from my_tool.fun_tool import add,sub,multiply

# math_agent = Agent(
#     name="math_agent",
#     instructions=" You are helpfull math_agent assistant. ",
#     tools=[add,sub,multiply],
#     model=GEMINI_MODEL
# )

# agent = Agent(
#     name="simple_agent",
#     instructions=" You are helpfull assistant. ",
#     tools=[math_agent.as_tool(
#         tool_name="math_agent",
#         tool_description="This is a math_tool",
#         )
#            ],
#     model=GEMINI_MODEL
# )


