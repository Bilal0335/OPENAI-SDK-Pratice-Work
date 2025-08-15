
# ! hook_run.py
from agents import Runner
from my_agent.run_hook_agent import hook_run_ag
from my_hook.my_run_hook import MyRunHook
import rich

hook_res = Runner.run_sync(
    starting_agent=hook_run_ag,
    input="2+2=?",
    context={"id":'123'},
    hooks=MyRunHook()
)

rich.print("\n[yellow]=== Final Result ===[/yellow]")
rich.print(f"[bold blue]Agent Name:[/bold blue] {hook_res.last_agent.name}")
rich.print(f"[bold yellow]Final Output:[/bold yellow] {hook_res.final_output}")
