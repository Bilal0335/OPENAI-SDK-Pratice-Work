from agents import RunContextWrapper
from my_data_type.data_type import EnglishData, MathData, MyhandoffData


# ! Customizing handoffs via the handoff() function
# 2. Handoff callback function
async def service(ctx:RunContextWrapper,input_data:MyhandoffData):
    print(ctx.context)
    print("Resoning: ",input_data.reason)
    print("Result: ",input_data.result)
    
    
# -------------------------------
# 2️⃣ Handoff Callback Functions
# -------------------------------

async def math_service(ctx: RunContextWrapper, input_data: MathData):
    print("=== Math Service Called ===")
    print("Context:", ctx.context)
    print("Reason:", input_data.reason)
    print("Math Value (before):", input_data.value)
    
    # Simple computation
    try:
        input_data.value = str(eval(input_data.value))  # demo only
    except Exception as e:
        input_data.value = f"Error: {e}"
    
    print("Math Value (after computation):", input_data.value)

async def english_service(ctx: RunContextWrapper, input_data: EnglishData):
    print("=== English Service Called ===")
    print("Context:", ctx.context)
    print("Reason:", input_data.reason)
    print("Text (before):", input_data.text)
    
    # Simple processing
    input_data.text = input_data.text.upper()
    
    print("Text (after processing):", input_data.text)
