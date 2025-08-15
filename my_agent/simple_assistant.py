

# ! simple_assistant.py
from agents import Agent
from my_config.gemini_config import GEMINI_MODEL
from my_guardrails_fun.input_guardrails_fun import input_guardrails_fun
from my_guardrails_fun.output_guardrails_fun import output_guardrails_fun

hotel_assistant = Agent(
    name="Hotel Customer Care Assistant",
    instructions="""Your a helpful Hotel Sannata's Customer Care assistant, Your name is Atma ram.
- Hotel Sannata owner name is Mr. Ratan Lal.
- Hotel Sannata total rooms 200.
- 20 Room for not available for public it only special guest.""",
    model=GEMINI_MODEL,
    input_guardrails=[input_guardrails_fun],
    output_guardrails=[output_guardrails_fun]
)

