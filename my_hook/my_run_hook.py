
# ! my_run_hook.py
from agents import AgentHooks, RunContextWrapper, Agent, TContext, Tool
from typing import Any
import rich


class MyRunHook(AgentHooks):
    
    async def on_agent_start(self, context: RunContextWrapper[TContext], agent: Agent) -> None:
        """Called before the agent is invoked. Called each time the current agent changes."""
        rich.print("\n[green]=== Start Run Hook ===[/green]")
        rich.print("[green]Agent Name:[/green]", agent.name)

    async def on_agent_end(
        self,
        context: RunContextWrapper[TContext],
        agent: Agent,
        output: Any,
    ) -> None:
        """Called when the agent produces a final output."""
        rich.print("\n[red]=== End Run Hook ===[/red]")
        rich.print("[red]Agent Name:[/red]", agent.name)
        rich.print("[red]Output:[/red]", output)
        
    async def on_handoff(
        self,
        context: RunContextWrapper[TContext],
        from_agent: Agent,
        to_agent: Agent,
    ) -> None:
        """Called when a handoff occurs."""
        rich.print("\n[cyan]=== Run Handoff Hook ===[/cyan]")
        rich.print("[cyan]From Agent Name:[/cyan]", from_agent.name)
        rich.print("[magenta]To Agent Name:[/magenta]", to_agent.name)
        
    async def on_tool_start(
        self,
        context: RunContextWrapper[TContext],
        agent: Agent,
        tool: Tool,
    ) -> None:
        """Called before a tool is invoked."""
        rich.print("\n[yellow]=== Start Tool Run Hook ===[/yellow]")
        rich.print("[yellow]Agent Name:[/yellow]", agent.name)
        rich.print("[yellow]Tool Name:[/yellow]", tool.name)
        rich.print("[yellow]Tool Description:[/yellow]", tool.description)

    async def on_tool_end(
        self,
        context: RunContextWrapper[TContext],
        agent: Agent,
        tool: Tool,
        result: str,
    ) -> None:
        """Called after a tool is invoked."""
        rich.print("\n[blue]=== End Tool Run Hook ===[/blue]")
        rich.print("[blue]Agent Name:[/blue]", agent.name)
        rich.print("[blue]Tool Name:[/blue]", tool.name)
        rich.print("[blue]Tool Result:[/blue]", result)
