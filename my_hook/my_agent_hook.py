

# ! my_agent_hook.py
from agents import AgentHooks, RunContextWrapper, Agent, TContext, Tool
from typing import Any
import rich, requests

class MyAgentHook(AgentHooks):
    
    async def on_start(self, context: RunContextWrapper, agent: Agent) -> None:
        """Called before the agent is invoked."""
        rich.print("\n[green]=== Start Agent Hook ===[/green]")
        rich.print("[green]Starting Agent:[/green]", agent.name)
        rich.print("[green]Start Context:[/green]", context.context)

        # Inject a custom value
        context.context['name'] = "Bilal Hussain"

        # Fetch data from API if 'id' exists in context
        user_id = context.context.get("id")
        if user_id:
            try:
                url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
                res = requests.get(url, timeout=5)
                res.raise_for_status()
                result = res.json()

                # Save fetched data in context
                context.context["obj"] = result

                rich.print(f"[cyan]Fetched User Data for ID {user_id}:[/cyan]", result)
            except requests.RequestException as e:
                rich.print(f"[red]API request failed:[/red] {e}")
        else:
            rich.print("[yellow]No 'id' found in context. Skipping API fetch.[/yellow]")
        
    async def on_end(
        self,
        context: RunContextWrapper,
        agent: Agent,
        output: Any,
    ) -> None:
        """Called when the agent produces a final output."""
        rich.print("\n[red]=== End Agent Hook ===[/red]")
        rich.print("[red]Agent Name:[/red]", agent.name)
        rich.print("[red]End Context:[/red]", context.context)
        rich.print("[red]Output:[/red]", output)
        
    async def on_tool_start(
        self,
        context: RunContextWrapper[TContext],
        agent: Agent,
        tool: Tool,
    ) -> None:
        """Called before a tool is invoked."""
        rich.print("\n[yellow]=== Start Tool Hook ===[/yellow]")
        rich.print("[yellow]Agent Name:[/yellow]", agent.name)
        rich.print("[yellow]Tool Name:[/yellow]", tool.name)

    async def on_tool_end(
        self,
        context: RunContextWrapper[TContext],
        agent: Agent,
        tool: Tool,
        result: str,
    ) -> None:
        """Called after a tool is invoked."""
        rich.print("\n[blue]=== End Tool Hook ===[/blue]")
        rich.print("[blue]Agent Name:[/blue]", agent.name)
        rich.print("[blue]Tool Name:[/blue]", tool.name)
        rich.print("[blue]Tool Result:[/blue]", result)
        
    async def on_handoff(
        self,
        context: RunContextWrapper[TContext],
        to_agent: Agent,
        from_agent: Agent,
    ) -> None:
        """Called when the agent is being handed off to."""
        rich.print("\n[cyan]=== Handoff Hook ===[/cyan]")
        rich.print("[cyan]From Agent Name:[/cyan]", from_agent.name)
        rich.print("[magenta]To Agent Name:[/magenta]", to_agent.name)

