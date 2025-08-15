
# ! my_config/groq_config.py
from agents import OpenAIChatCompletionsModel,AsyncOpenAI
from decouple import config

key = config("GROQ_API_KEY")
base_url = config("BASE_URL_GROQ")

groq_client = AsyncOpenAI(
    api_key=key,
    base_url=base_url
)

GROQ_MODEL = OpenAIChatCompletionsModel(
    openai_client=groq_client,
    model="llama-3.3-70b-versatile"
    #  model="gemini-2.5-flash",
)

