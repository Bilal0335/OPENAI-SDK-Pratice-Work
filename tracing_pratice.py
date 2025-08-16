from agents import (
    OpenAIChatCompletionsModel,
    Agent,
    Runner,
    AsyncOpenAI,
    set_tracing_disabled,
    RunConfig,
    set_trace_processors,
    trace
)
from agents.tracing.processors import ConsoleSpanExporter,BatchTraceProcessor,default_processor
from agents.tracing.processor_interface import TracingExporter
from agents.tracing.spans import Span
from agents.tracing.traces import Trace
import os,rich
from dotenv import load_dotenv
load_dotenv()




class CustomConsoleSpanExporter(TracingExporter):
    def export(self, items: list[Trace | Span]):
        for item in items:
            if isinstance(item, Trace):
                print(f"[Trace] ID: {item.trace_id} | Name: {item.name}")
            elif item.span_data.type == "generation":
                usage = item.span_data.usage or {}
                model = item.span_data.model
                user_input = item.span_data.input or []
                output = item.span_data.output or []

                print("🧠 Model Used:", model)
                print("📥 Input Tokens:", usage.get("input_tokens", "N/A"))
                print("📤 Output Tokens:", usage.get("output_tokens", "N/A"))

                if user_input:
                    print("🙋 User Asked:", user_input[-1].get("content", "N/A"))
                if output:
                    print("🤖 Bot Replied:", output[0].get("content", "N/A"))


# exporter = ConsoleSpanExporter() # or use BackendSpanExporter()
exporter = CustomConsoleSpanExporter() 
processor = BatchTraceProcessor(exporter)


# set_tracing_disabled(disabled=True)
set_trace_processors(
            [processor,
                    #   default_processor() # sent to the dashbaord openai
                      ]
                    ) # override default processor(s)

gemini_api_key = os.getenv("GEMINI_API_KEY")
base_url = os.getenv("BASE_URL_GEMINI")



external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url=base_url
)

model = OpenAIChatCompletionsModel(
    openai_client=external_client,
    model="gemini-2.0-flash"
)


agent = Agent(
    name="SImple Agent",
    instructions="You are helpfull assistant.",
    model=model
)

# res = Runner.run_sync(
#     agent,
#     input="Hello, what is ai?",  
# )

# ✅ STEP 5: Wrap in a custom trace
with trace("Bilal workflow"):
    result = Runner.run_sync(
        agent,
        input="how are you"
    )

rich.print(result.final_output)