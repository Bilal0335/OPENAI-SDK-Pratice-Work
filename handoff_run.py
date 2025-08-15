# multi_agent_handoff_clean.py
from agents import Agent, handoff, Runner, RunContextWrapper
from pydantic import BaseModel
import rich
from my_config.gemini_config import GEMINI_MODEL
from my_tool.fun_tool import add
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX

# -------------------------------
# 1️⃣ Handoff Input Models
# -------------------------------

class MathData(BaseModel):
    reason: str
    value: str

class EnglishData(BaseModel):
    text: str
    reason: str

class MyhandoffData(BaseModel):
    reason: str
    result: str

# -------------------------------
# 2️⃣ Handoff Callback Functions
# -------------------------------

async def math_service(ctx: RunContextWrapper, input_data: MathData):
    print("=== Math Service Called ===")
    print("Context:", ctx.context)
    print("Reason:", input_data.reason)
    print("Math Value (before):", input_data.value)
    
    # Simple computation
    try:
        input_data.value = str(eval(input_data.value))  # demo only
    except Exception as e:
        input_data.value = f"Error: {e}"
    
    print("Math Value (after computation):", input_data.value)

async def english_service(ctx: RunContextWrapper, input_data: EnglishData):
    print("=== English Service Called ===")
    print("Context:", ctx.context)
    print("Reason:", input_data.reason)
    print("Text (before):", input_data.text)
    
    # Simple processing
    input_data.text = input_data.text.upper()
    
    print("Text (after processing):", input_data.text)

async def service(ctx: RunContextWrapper, input_data: MyhandoffData):
    print("=== Generic Service Called ===")
    print("Context:", ctx.context)
    print("Reason:", input_data.reason)
    print("Result:", input_data.result)

# -------------------------------
# 3️⃣ Create Agents
# -------------------------------

math_agent = Agent(name="Math Agent", model=GEMINI_MODEL)
english_agent = Agent(name="English Agent", model=GEMINI_MODEL)

# -------------------------------
# 4️⃣ Setup Handoffs (with proper service)
# -------------------------------

math_handoff = handoff(
    agent=math_agent,
    tool_name_override="math_teacher",
    tool_description_override="Handles math questions",
    on_handoff=math_service,
    input_type=MathData
)

english_handoff = handoff(
    agent=english_agent,
    tool_name_override="english_teacher",
    tool_description_override="Handles English questions",
    on_handoff=english_service,
    input_type=EnglishData
)

# -------------------------------
# 5️⃣ Create Main Assistant
# -------------------------------

assistant = Agent(
    name="Assistant",
    instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
        You are a general assistant.
        If the question is about Math, hand off to math_agent.
        If the question is about English, hand off to english_agent.
        Otherwise answer yourself.
    """,
    model=GEMINI_MODEL,
    handoffs=[math_handoff, english_handoff]
)

# -------------------------------
# 6️⃣ Run Assistant with Inputs
# -------------------------------

# Example 1: Math question
res_math = Runner.run_sync(
    starting_agent=assistant,
    input="2 + 3 * 4",
    context={"name": "Bilal", "age": 25}
)

rich.print("Final Output (Math):", res_math.final_output)
rich.print("Last Agent:", res_math.last_agent.name)

# Example 2: English question
res_english = Runner.run_sync(
    starting_agent=assistant,
    input="write a essay pakistan.",
    context={"name": "Bilal", "age": 25}
)

rich.print("Final Output (English):", res_english.final_output)
rich.print("Last Agent:", res_english.last_agent.name)
