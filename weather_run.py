
# ! weather_run.py
from agents import Runner
# from my_agent.weather_agent import simple_agent
# from my_agent.weather_agent import math_agent
# from my_agent.weather_agent import recipe_agent
from my_agent.weather_agent import demo_agent
import rich

# Run the agent
# result = Runner.run_sync(simple_agent, "What is the weather in Karachi?")

# rich.print("[bold green]Agent Name:[/]", result.last_agent.name)
# rich.print("[bold yellow]Final Output:[/]", result.final_output)



# res1 = Runner.run_sync(math_agent, "Add 5 and 7")
# res2 = Runner.run_sync(math_agent, "Divide 11 by 10")

# rich.print("[bold green]Agent Name:[/]", res1.last_agent.name)
# rich.print("[bold yellow]Output 1:[/]", res1.final_output)
# rich.print("[bold red]Output 2:[/]", res2.final_output)





# res1 = Runner.run_sync(recipe_agent, "Get recipe for chocolate")
# res2 = Runner.run_sync(recipe_agent, "Get recipe for xyz")

# rich.print("[bold green]Agent Name:[/]", res1.last_agent.name)
# rich.print("[bold yellow]Output 1:[/]", res1.final_output)
# rich.print("[bold red]Output 2 (Error):[/]", res2.final_output)













rich.print("[bold blue]--- DEFAULT ERROR TOOL ---[/]")
res1 = Runner.run_sync(demo_agent, "default_error_tool 5")
rich.print("Output:", res1.final_output)

rich.print("[bold blue]--- CUSTOM ERROR TOOL ---[/]")
res2 = Runner.run_sync(demo_agent, "custom_error_tool 5")
rich.print("Output:", res2.final_output)

rich.print("[bold blue]--- NONE ERROR TOOL ---[/]")
try:
    res3 = Runner.run_sync(demo_agent, "none_error_tool 5")
    rich.print("Output:", res3.final_output)
except Exception as e:
    rich.print("[bold red]Manual Handling Output:[/]", str(e))
