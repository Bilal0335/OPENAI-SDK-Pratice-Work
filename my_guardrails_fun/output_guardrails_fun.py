
# ! output_guardrails_fun.py
from agents import (
    GuardrailFunctionOutput,
    RunContextWrapper,
    output_guardrail,
    Runner,
    Agent
)
from my_agent.guard_agent import guardrails_agnet

@output_guardrail
async def output_guardrails_fun(ctx:RunContextWrapper[None],agent:Agent,output)-> GuardrailFunctionOutput:
    
    result = await Runner.run(guardrails_agnet,input=output,context=ctx.context)
    
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_hotel_sannata_account_or_tax_query
    )
    
