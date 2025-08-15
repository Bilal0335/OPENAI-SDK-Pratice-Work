
# ! my_runner/runner.py
from my_config.gemini_config import gemini_client,GEMINI_MODEL
from agents import RunConfig

config = RunConfig(
        model_provider=gemini_client,
        model=GEMINI_MODEL
    )

#  run-level configuration