
# ! my_agent/shopping_agent.py
from agents import Runner,set_tracing_disabled
import rich
from my_agent.shopy_agent  import shopping_agents_tool


# enable_verbose_stdout_logging()
set_tracing_disabled(disabled=True)

tool_res = Runner.run_sync(
    starting_agent=shopping_agents_tool,
    input="Show me the price of Nike AIR max shoes and how many total products do you have"
)

rich.print(f"[bold green] {tool_res.final_output} [/bold green]")
