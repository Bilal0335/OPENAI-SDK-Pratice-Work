from agents import RunContextWrapper




async def tool_validated(ctx:RunContextWrapper,agent):
    if ctx.context["age"]>=18:
        return True
    else:
        return False