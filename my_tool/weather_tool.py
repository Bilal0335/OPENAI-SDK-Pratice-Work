


# ! weather_tool.py
from agents import function_tool, RunContextWrapper
from agents.exceptions import UserError
from typing import Any

def custom_error_function(ctx: RunContextWrapper[Any], error: Exception) -> str:
    """Custom error handler for tools"""
    print(f"[Tool Error] {error}")
    return f"Oops! Something went wrong while fetching weather: {str(error)}"

@function_tool(
    name_override="get_weather",
    description_override="Weather ka data le ao",
    use_docstring_info=True,
    failure_error_function=custom_error_function
)

async def fetch_weather(city: str) -> str:
    """
    Fetch weather for a given city.
    """
    # Simulate failure
    if city.lower() == "karachi":
        raise UserError("Weather API failed for Karachi!")
    return f"The weather in {city} is sunny with 40C."
