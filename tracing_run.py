
# ! tracing_run.py
from agents import Runner,set_tracing_export_api_key
from decouple import config
from my_agent.tracing_agent import trace_agent
import rich

openai_key = config("OPEN_API_KEY")
set_tracing_export_api_key(openai_key)

tracing_res = Runner.run_sync(
    starting_agent=trace_agent,
    input="what is 2+2=??"
)

rich.print(f"[bold green] Agent Name: {tracing_res.last_agent.name} [/bold green]")
rich.print(f"[bold yellow] Final Output: {tracing_res.final_output} [/bold yellow]")
