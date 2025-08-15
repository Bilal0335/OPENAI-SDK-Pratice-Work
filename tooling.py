
# ! my_agent/shopping_agent.py
from agents import Runner,set_tracing_disabled
from my_agent.tool_agent import math_tool_agents
import rich
# from my_agent.shopping_agent import shopping_agents_tool


# enable_verbose_stdout_logging()
set_tracing_disabled(disabled=True)

tool_res = Runner.run_sync(
    starting_agent=math_tool_agents,
    input="current today date?"
)

rich.print(f"[bold green] {tool_res.final_output} [/bold green]")

# questions = [
#     "what is 2 + 5=? and multiply by 100",
#     "10 - 3 ka answer do",
#     "15 * 4 kitna hota hai?",
#     "today date batao",
#     "what is the weather in Lahore?"
# ]

# # Har question ko run karo
# for q in questions:
#     tool_res = Runner.run_sync(
#         starting_agent=math_tool_agents,
#         input=q
#     )
#     rich.print(f"[bold yellow]Q:[/bold yellow] {q}")
#     rich.print(f"[bold green]A:[/bold green] {tool_res.final_output}")
#     print("-" * 50)


# result = Runner.run_sync(
#     shopping_agents_tool,
#     "Show me the price of Nike AIR max shoes and how many total products do you have",
# )

# rich.print(result.final_output)