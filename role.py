
# # ! role.py
# from agents import Runner,set_tracing_disabled
# from my_agent.role_agent import role_agent
# from my_data_type.data_type import UserData
# import rich

# set_tracing_disabled(disabled=True)

# # test with Student
# student_context = UserData(
#     name="Ali",
#     age=20,
#     role="student"
# )

# student_res = Runner.run_sync(
#     role_agent,
#     input="Explain what is Javascript programming?",
#     context=student_context
# )
# rich.print(student_res.final_output)

# # Test with Teacher
# teacher_context = UserData(
#     name="Nabeel",
#     age=35,
#     role="Teacher"
# )

# teacher_res = Runner.run_sync(
#     role_agent,
#     input="Explain what is Python programming?",
#     context=teacher_context
# )
# # rich.print(teacher_res.final_output)


# ! role.py
from agents import Runner, set_tracing_disabled
from my_agent.role_agent import role_agent
from my_data_type.data_type import UserData
import rich

set_tracing_disabled(disabled=True)

# Test users
test_users = [
    UserData(name="Ali", age=20, role="student"),
    UserData(name="Nabeel", age=35, role="teacher")
]

# Inputs to test for each user
inputs = [
    "Explain what is JavaScript programming?",
    "Explain what is Python programming?"
]

# Run tests
for user, prompt in zip(test_users, inputs):
    res = Runner.run_sync(
        role_agent,
        input=prompt,
        context=user
    )
    rich.print(f"[bold green]--- Result for {user.role.title()} ({user.name}) ---[/bold green]")
    rich.print(res.final_output)
    print("\n")
