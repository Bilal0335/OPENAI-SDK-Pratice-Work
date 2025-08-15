
# ! input_guardrails_fun.py
from agents import (
    GuardrailFunctionOutput,
    RunContextWrapper,
    TResponseInputItem,
    input_guardrail,
    Runner,
    Agent
)
import rich
from my_agent.guard_agent import guardrails_agnet

@input_guardrail
async def input_guardrails_fun(ctx:RunContextWrapper[None],agent:Agent,input: str | list[TResponseInputItem])-> GuardrailFunctionOutput:
    rich.print(agent)
    result = await Runner.run(guardrails_agnet,input=input,context=ctx.context)
    
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=not result.final_output.is_hotel_sannata_query
    )
    
