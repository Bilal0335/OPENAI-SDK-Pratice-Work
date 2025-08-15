
# ! tran_agent.py
from agents import Runner
from my_agent.translate_as_tool_agent import math_agent
import rich

# ! custom function tools 
res = Runner.run_sync(
    starting_agent=math_agent,
    input="51-1=?",
    context={
        "name":"Bilal",
        "age":12,
        "role":"Student"
    }
)

rich.print("Final Output:",res.final_output)

# ! Controlling tool use behavior and tool choice 

# res = Runner.run_sync(
#     starting_agent=math_agent,
#     input="5+5 = ? jo be answer ay multiply kr dou 10 jo be answer ay us ma substract kr dou 90",
#     # input="hi",
#     # input="10+5"
#     # input="5+5 ka answer nikal ke multiply karo 10",
#     max_turns=5
# )
# rich.print("Final Output:", res.final_output)

# ! as_tool
# from my_agent.translate_as_tool_agent import orchestrator_agent
# translate_res = Runner.run_sync(
#     starting_agent=orchestrator_agent,
#     input="Say 'Hello, how are you?' in Spanish."
# )

# rich.print("Final Output:", translate_res.final_output)
