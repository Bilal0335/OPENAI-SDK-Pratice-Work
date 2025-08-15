

# ! my_agent/teacher_agent.py
from agents import Agent
from my_config.gemini_config import GEMINI_MODEL
from my_config.groq_config import GROQ_MODEL
# from my_data_type.data_type import MyData,CalendarEvent,WeatherReport
from my_tool.my_tools import get_age
from my_instruction.dynamic_instruction import dynamic_instruction
from my_data_type.data_type import UserData

# ! context management partice work
context_agent = Agent[UserData](
    name="context_agent",
    instructions=dynamic_instruction,
    model=GEMINI_MODEL,
    tools=[get_age],
    tool_use_behavior="stop_on_first_tool"
)

# ! output_type pratice work 

# gemini_agent = Agent(
#     name="gemini_agent",
#     instructions="You are helpfull assistnat.",
#     model=GEMINI_MODEL,
#     output_type=MyData
# )

# calendar_agent = Agent(
#     name="Calendar extractor",
#     instructions="Extract calendar events from the given text and return it in structured format.",
#     model=GEMINI_MODEL,
#     output_type=CalendarEvent
# )

# weather_agent = Agent(
#     name="Weather agent",
#     instructions = """
#         You are a weather data extractor.
#         From the given text, extract:
#         - city name (string)
#         - temperature in Celsius (float)
#         - weather condition (string like 'Sunny', 'Cloudy', 'Rainy', etc.)

#         Return the result strictly in the given structured format without any extra text.
# """
# ,
#     model=GEMINI_MODEL,
#     output_type=WeatherReport
# )

# bookinfo_agent = Agent(
#     name="bookinfo_agent",
#     instructions = """
#         You are a book information extractor.
#         From the given text, extract:
#         - title (string)
#         - author (string)
#         - year of publication (integer)
#         - genres (list of strings) — each genre should start with a capital letter.

#         Return the result strictly in the structured format defined by the BookInfo model, without any extra words or explanation.
# """
# ,
#     model=GEMINI_MODEL
# )

# ! gemini_agent & groq_agent
# gemini_agent = Agent(
#     name="gemini_agent",
#     instructions="You are helpfull assistnat.",
#     model=GEMINI_MODEL
# )

# groq_agent = Agent(
#     name="groq_agent",
#     instructions="You are helpfull assistnat.",
#     model=GROQ_MODEL
# )