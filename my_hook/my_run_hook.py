

# ! my_run_hook.py
from agents import AgentHooks, RunContextWrapper, Agent, TContext, Tool
from typing import Any
import rich


class MyRunHook(AgentHooks):
    
    async def on_agent_start(self, context: RunContextWrapper[TContext], agent: Agent) -> None:
        """Called before the agent is invoked. Called each time the current agent changes."""
        rich.print("[green]Start Run Hook[/green]")
        rich.print("[green]Agent Name: [/green]",agent.name)

    async def on_agent_end(
        self,
        context: RunContextWrapper[TContext],
        agent: Agent,
        output: Any,
    ) -> None:
        """Called when the agent produces a final output."""
        rich.print("[red]End Run Hook[/red]")
        rich.print("[red]Agent Name: [/red]",agent.name)
        rich.print("[red]Output:[/red]", output)
 
