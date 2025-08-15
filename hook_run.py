
# ! hook_run.py
from agents import Runner
from my_agent.agent_hook import hook_agent
import rich

hook_res = Runner.run_sync(
    starting_agent=hook_agent,
    input="2+2=?",
    context={"id":"3"}
)

rich.print(f"[bold green]Agent Name:[/bold green] {hook_res.last_agent.name}")
rich.print(f"[bold yellow]Final Output:[/bold yellow] {hook_res.final_output}")
