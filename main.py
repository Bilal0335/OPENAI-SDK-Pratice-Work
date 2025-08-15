
# ! main.py
from agents import Runner,set_tracing_disabled
from my_agent.teacher_agent import context_agent
from my_data_type.data_type import UserData
import rich
set_tracing_disabled(True)

user1 = UserData(
        name = "akmal",
        age =  22,
        role = "Student"
)

# ! context management

context_res = Runner.run_sync(
    context_agent,
    input="what is age of user?",
    context=user1
    # context={
    #     "name":"nabeel",
    #     "age": 22,
    #     "role":"Student"
    # }
    # context=["Bilal","akmal"]
    # context="Bilal"
)
rich.print(context_res.final_output)

# ! output_type pratice work

# bookinfo_res = Runner.run_sync(
#     starting_agent=bookinfo_agent,
#     input="Harry Potter and the Philosopher's Stone is a fantasy novel written by J.K. Rowling in 1997. It belongs to the genres fantasy and adventure."
# )

# rich.print(bookinfo_res.final_output)

# weather_res = Runner.run_sync(
#     starting_agent=weather_agent,
#     input="Today in Karachi the weather is sunny with a temperature of 34.5°C."
# )

# rich.print(weather_res.final_output)

# res1 = Runner.run_sync(
#     starting_agent=gemini_agent,
#     input="2+2=? explain in detail",
# )
# rich.print(res1.final_output)



# calendar_res = Runner.run_sync(
#     starting_agent=calendar_agent,
#     input="Meeting about Project Alpha on 2025-08-12 with Alice, Bob, and Charlie."
# )
# rich.print(calendar_res.final_output)

# ! configartion layer
# from my_agent.teacher_agent import groq_agent,gemini_agent
# from my_config.gemini_config import gemini_client
# from agents import Runner,set_default_openai_api,set_default_openai_key
# from my_runner.runner import RunConfig

# import rich

# set_default_openai_api("chat_completions")
# set_default_openai_key(gemini_client)

# res1 = Runner.run_sync(
#     starting_agent=gemini_agent,
#     input="2+2=? explain in detail",
#     # run_config=RunConfig # run-level configuration
# )
# rich.print(res1.final_output)



# # res2 = Runner.run_sync(
# #     starting_agent=groq_agent,
# #     input="2+2=? explain in detail"
# # )
# # rich.print(res2.final_output)