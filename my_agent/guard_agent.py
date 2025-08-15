from my_data_type.data_type import Hoteldata
from agents import Agent 
from my_config.gemini_config import GEMINI_MODEL


guardrails_agnet = Agent(
    name="Hotel Customer Care Assistant",
    instructions="""Check Hotel Sannata's querries  and account or tex query""",
    model=GEMINI_MODEL,
    output_type=Hoteldata,
)
