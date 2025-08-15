

# ! weather_agent.py
from agents import Agent
# from my_tool.weather_tool import fetch_weather
# from my_tool.fun_tool import add_numb,divide_numbers
from my_tool.fun_tool import get_recipe
from my_config.gemini_config import GEMINI_MODEL

# ! simple_agent = Agent(
#     name="Simple Assistant",
#     instructions="You are a helpful assistant that can fetch weather.",
#     tools=[fetch_weather],
#     model=GEMINI_MODEL
# )



# ! math_agent

# math_agent = Agent(
#     name="Math Helper Agent",
#     instructions="You can add or divide numbers and handle errors",
#     tools=[add_numb, divide_numbers],
#     model=GEMINI_MODEL
# )


# # ! recipe_agent
# recipe_agent = Agent(
#     name="Recipe Suggester",
#     instructions="You provide recipe based on ingredient",
#     model=GEMINI_MODEL,
#     tools=[get_recipe]
# )


from agents import Agent
from my_tool.fun_tool import default_error_tool, custom_error_tool, none_error_tool

demo_agent = Agent(
    name="Error Handling Demo Agent",
    instructions="This agent demonstrates default, custom, and None error handling.",
    tools=[default_error_tool, custom_error_tool, none_error_tool],
    model=GEMINI_MODEL
)
