
# ! my_tool/math_tool.py

from datetime import datetime
from agents import function_tool,Agent,FunctionTool,RunContextWrapper
import rich
from my_config.gemini_config import GEMINI_MODEL
from my_data_type.data_type import MyToolSchema
from validators.valid_tool import tool_validated
from agents.exceptions import UserError
from typing import Any
import requests

# ! custom FunctionTool

async def substract_fun(ctx:RunContextWrapper,arg:str):
    obj = MyToolSchema.model_validate_json(arg)
    res = obj.n1 - obj.n2
    print(F"substract called")
    return f"Your answer is {res}"

substract = FunctionTool(
    name="substract",
    description="This is substract function",
    params_json_schema=MyToolSchema.model_json_schema(),
    on_invoke_tool=substract_fun,
    # is_enabled=False
    is_enabled=tool_validated
)

# ! as_tool
spanish_agent = Agent(
    name="Spanish agent",
    instructions="You translate the user's message to Spanish",
    model=GEMINI_MODEL
)

french_agent = Agent(
    name="French agent",
    instructions="You translate the user's message to French",
    model=GEMINI_MODEL
)

# !function_tool

@function_tool
async def add(n1:int,n2:int)->str:
    """this is add function
        arg:
            n1:int
            n2:int
        return str
    """
    print("Add function is called -->")
    return f"You answer is {n1+n2}"


# @function_tool
# async def sub(n1:int,n2:int)->str:
#     """this is sub function
#         arg:
#             n1:int
#             n2:int
#         return str
#     """
#     print("Substract function is called -->")

#     return f"You answer is {n1-n2}"


@function_tool
async def multiply(n1:int,n2:int)->str:
    """this is multiply function
        arg:
            n1:int
            n2:int
        return str
    """
    print("Multiply function is called -->")
    return f"You answer is {n1*n2}"

@function_tool
async def get_date():
    _now = datetime.now()
    return _now.strftime("the date is %d-%m-%y")

@function_tool
async def get_weather(city:str)->str:
    """this is get_weather function"""
    print("get_weather function is called -->")
    return f"the weather of {city} is sunny"


@function_tool
async def shopping_tool(query:str)->str:
    """this is shopping_agent function"""
    api_url = "https://template-03-api.vercel.app/api/products"
    response = requests.get(api_url)
    data = response.json()
    
    products = data.get("data",[])
    return "\n".join([f"{i+1}. {item['productName']} - Rs {item['price']}" for i, item in enumerate(products)])


# WEATHER
@function_tool
async def weather(city: str) -> str:
    """Get weather for a city"""
    print("Weather tool called -->")
    return f"The weather in {city} is sunny."




# custon handling error 

# from agents.exceptions import UserError
# from typing import Any

def math_error(ctx:RunContextWrapper[Any],error:Exception)->str:
    """This is math_error function"""
    rich.print("math_error function is called -->")
    rich.print(f"[Math Tool Error]: {error}")
    return f"Math error occured: {str(error)}"


@function_tool(
    name_override="add_number",
    description_override="Add two number",
    failure_error_function=math_error
)
async def add_numb(a:int,b:int)->str:
    rich.print("Add Tool Called-->")
    return f"Sum is: {a+b}"


@function_tool(
    name_override="divide_numbers",
    description_override="Divide two numbers",
    failure_error_function=math_error
)
async def divide_numbers(a: float, b: float) -> str:
    if b == 0:
        raise UserError("Cannot divide by zero!")
    return f"Division result: {a / b}"



def recipe_error(ctx: RunContextWrapper[Any], error: Exception) -> str:
    print(f"[Recipe Tool Error]: {error}")
    return "Recipe could not be found. Please try a different ingredient."

recipes_db = {
    "chocolate": "Chocolate Cake Recipe...",
    "tomato": "Tomato Soup Recipe..."
}

@function_tool(failure_error_function=recipe_error)
async def get_recipe(ingredient: str) -> str:
    if ingredient.lower() not in recipes_db:
        raise UserError(f"No recipe found for {ingredient}")
    return recipes_db[ingredient.lower()]




# ---------------- Default Error ----------------
@function_tool()
async def default_error_tool(x: int) -> str:
    """This tool raises error, default error handling is used."""
    raise UserError("Default tool failed!")

# ---------------- Custom Error ----------------
def custom_error(ctx: RunContextWrapper[Any], error: Exception) -> str:
    return f"Custom error occurred: {str(error)}"

@function_tool(failure_error_function=custom_error)
async def custom_error_tool(x: int) -> str:
    """This tool raises error, custom error handling is used."""
    raise UserError("Custom tool failed!")

# ---------------- None (Manual Handling) ----------------
@function_tool(failure_error_function=None)
async def none_error_tool(x: int) -> str:
    """This tool raises error, manual handling required."""
    raise UserError("None tool failed!")