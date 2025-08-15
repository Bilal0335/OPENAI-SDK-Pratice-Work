

# ! guard_run.py
from agents import Runner,InputGuardrailTripwireTriggered,OutputGuardrailTripwireTriggered
from my_agent.simple_assistant import hotel_assistant
from my_agent.guard_agent import guardrails_agnet
import rich

# propmt = input("Enter Quries Hotel Sannata's: ")

try:
    guardrail_run = Runner.run_sync(
    starting_agent=hotel_assistant,
    input="How many room in Hotel Sannata's?"
    )

    rich.print(f"[bold green] Final Output: {guardrail_run.final_output} [/bold green]")

except InputGuardrailTripwireTriggered as e:
    rich.print(f"[bold red] Error: {e} [/bold red]")

except OutputGuardrailTripwireTriggered as e:
    rich.print(f"[bold red] Error: {e} [/bold red]")
