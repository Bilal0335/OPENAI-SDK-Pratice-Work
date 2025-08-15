# main.py
from agents import Runner
from my_agent.handoff_agent import assistant
import rich

# Test run
handsoff_res = Runner.run_sync(
    starting_agent=assistant,
    input="lahore ka mosam kesa hai and 2 + 2 = ??",
    context={
        "name": "Bilal",
        "age": 14
    }
)

rich.print("\nAgent Name:", handsoff_res.last_agent.name)
rich.print("\nFinal Output:", handsoff_res.final_output)


# ! Prtatice 
# from agents import Agent, RunContextWrapper

# # Create agent
# agent = Agent(name="math_helper", instructions="Solve math problems.")

# # Make a fake run context for testing
# run_context = RunContextWrapper(agent=agent, input="Test prompt")

# # Now call get_system_prompt with context
# print("\n\n\nget_system_prompt Output:--> ", agent.get_system_prompt(run_context))

# -------------------------------
# 6️⃣ Run Assistant with Inputs
# -------------------------------

#! Example 1: Math question
# res_math = Runner.run_sync(
#     starting_agent=assistant,
#     input="2 + 3 * 4",
#     context={"name": "Bilal", "age": 25}
# )

# rich.print("Final Output (Math):", res_math.final_output)
# rich.print("Last Agent:", res_math.last_agent.name)

#! Example 2: English question
# res_english = Runner.run_sync(
#     starting_agent=assistant,
#     input="Translate 'Hello World' to Urdu",
#     context={"name": "Bilal", "age": 25}
# )

# rich.print("Final Output (English):", res_english.final_output)
# rich.print("Last Agent:", res_english.last_agent.name)
