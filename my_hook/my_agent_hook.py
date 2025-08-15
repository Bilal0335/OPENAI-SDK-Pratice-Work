# ! my_agent_hook.py
from agents import AgentHooks, RunContextWrapper, Agent, TContext, Tool
from typing import Any
import rich,requests


class MyAgentHook(AgentHooks):
    
    async def on_start(self, context: RunContextWrapper, agent: Agent) -> None:
        """Called before the agent is invoked."""
        rich.print("[green]Start Agent Hook[/green]")
        rich.print("[green]Starting Agent: [/green]",agent.name)
        rich.print("[green]Start Context[/green]",context.context)
        context.context['name'] = "Bilal Hussain"
        url = f"https://jsonplaceholder.typicode.com/users/{context.context['id']}"
        res = requests.get(url)
        result = res.json()
        context.context["obj"] = result
    async def on_end(
        self,
        context: RunContextWrapper,
        agent: Agent,
        output: Any,
    ) -> None:
        """Called when the agent produces a final output."""
        rich.print("[red]End Agent Hook[/red]")
        rich.print("[red]Starting Agent Hook[/red]:",agent.name)
        rich.print("[red]End Context[/red]",context.context)
        
    # async def on_tool_start(
    #     self,
    #     context: RunContextWrapper[TContext],
    #     agent: Agent,
    #     tool: Tool,
    # ) -> None:
    #     """Called before a tool is invoked."""
    #     rich.print("[blue]Start Tool Hook[/blue]")

    # async def on_tool_end(
    #     self,
    #     context: RunContextWrapper[TContext],
    #     agent: Agent,
    #     tool: Tool,
    #     result: str,
    # ) -> None:
    #     """Called after a tool is invoked."""
    #     rich.print("[blue]End Tool Hook[/blue]")
        
    # async def on_handoff(
    #     self,
    #     context: RunContextWrapper[TContext],
    #     agent: Agent,
    #     source: Agent,
    # ) -> None:
    #     """Called when the agent is being handed off to."""
    #     rich.print("[yellow]Handoff Hook[/yellow]")
    
    # ! customize 