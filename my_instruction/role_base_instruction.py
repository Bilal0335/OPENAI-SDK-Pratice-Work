
# # from agents import Agent,RunContextWrapper
# # from my_data_type.data_type import UserData


# # # ! pratice work
# # def role_based_instruction(ctx:RunContextWrapper[UserData],agent:Agent[UserData]):
# #     """Instructions change based on role in context"""
# #     user_name = ctx.context.name
# #     role = ctx.context.role.lower()
# #     if  role == "student":
# #         return f"User {user_name} is a student. Explain concepts step-by-step in simple words."
# #     elif role == "teacher":
# #         return f"User {user_name} is a teacher. Give short, professional summaries."
# #     else:
# #         return f"User {user_name} is a guest. Be friendly and helpful."

# from agents import Agent, RunContextWrapper
# from my_data_type.data_type import UserData

# def role_based_instruction(ctx: RunContextWrapper[UserData], agent: Agent[UserData]):
#     """Return dynamic instructions based on user role."""
#     user_name = ctx.context.name
#     user_age = ctx.context.age
#     role = ctx.context.role.lower()

#     return f"""
# You are a helpful assistant. Adapt your explanation based on the user's role.

# If the role is "student":
# - Use simple, beginner-friendly examples.
# - Avoid technical jargon unless explained.

# If the role is "teacher":
# - Provide more detailed and technical explanations.
# - Use precise terminology and assume the user has some background knowledge.

# User details:
# Name: {user_name}
# Age: {user_age}
# Role: {role}
# """


from agents import Agent, RunContextWrapper
from my_data_type.data_type import UserData

def role_based_instruction(ctx: RunContextWrapper[UserData], agent: Agent[UserData]):
    """Return dynamic instructions based on user role."""
    user_name = ctx.context.name
    user_age = ctx.context.age
    role = ctx.context.role.lower()

    # General instruction block
    base_instruction = f"""
You are a helpful assistant. Adapt your explanation based on the user's role.

If the role is "student":
- Use simple, beginner-friendly examples.
- Avoid technical jargon unless explained.

If the role is "teacher":
- Provide more detailed and technical explanations.
- Use precise terminology and assume the user has some background knowledge.

If the role is "guest":
- Be friendly, engaging, and easy to understand.

User details:
Name: {user_name}
Age: {user_age}
Role: {role}
"""

    # Role-specific addition
    if role == "student":
        role_specific = f"User {user_name} is a student. Explain concepts step-by-step in simple words."
    elif role == "teacher":
        role_specific = f"User {user_name} is a teacher. Give short, professional summaries."
    else:
        role_specific = f"User {user_name} is a guest. Be friendly and helpful."

    # Combine both
    return base_instruction + "\n" + role_specific
