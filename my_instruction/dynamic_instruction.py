

# ! instruction/dynamic_instruction.py

from agents import Agent,RunContextWrapper
from my_data_type.data_type import UserData


# ! pratice work
def dynamic_instruction(ctx:RunContextWrapper[UserData],agent:Agent[UserData]):
    """Instructions change based on role in context"""
    user_name = ctx.context.name
    role = ctx.context.role.lower()
    if  role == "student":
        return f"User {user_name} is a student. Explain concepts step-by-step in simple words."
    elif role == "teacher":
        return f"User {user_name} is a teacher. Give short, professional summaries."
    else:
        return f"User {user_name} is a guest. Be friendly and helpful."



# def dynamic_instruction(ctx:RunContextWrapper[UserData],agent:Agent[UserData]):
#     return f"username is {ctx.context.name}, Your are helpfull assistant"


# def dynamic_instruction(ctx:RunContextWrapper,agent):
#     return f"username is {ctx.context['name']}, Your are helpfull assistant"