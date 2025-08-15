
# ! my_config/gemini_config.py
from decouple import config
from agents import AsyncOpenAI,set_tracing_disabled,OpenAIChatCompletionsModel

key = config("GEMINI_API_KEY")
base_url = config("BASE_URL_GEMINI")

set_tracing_disabled(disabled=True)

gemini_client = AsyncOpenAI(
    api_key=key,
    base_url=base_url,
) #openai-key

GEMINI_MODEL=OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=gemini_client
)  #chat-completion