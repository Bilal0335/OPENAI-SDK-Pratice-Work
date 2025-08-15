

# ! my_tool/my_tools.py
from agents import RunContextWrapper,function_tool
from my_data_type.data_type import UserData

# ! pratice work
@function_tool
def get_age(ctx:RunContextWrapper[UserData]):
    """Return User Age"""
    name = ctx.context.name
    age = ctx.context.age
    return f"{name} is {age} year old" 




# @function_tool
# def get_age(ctx:RunContextWrapper[UserData]):
#     """Age function"""
#     print("Age function tool")
#     # print("ctx>>>",ctx.context['name'])
#     # return f"Your age is {ctx.context['age']}"
#     return f"Your age is {ctx.context.age}"