# app.py
import streamlit as st
import asyncio
from agents import Agent, Runner
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX

# <-- Update this import if your GEMINI_MODEL config is elsewhere -->
from my_config.gemini_config import GEMINI_MODEL

# --------------------------
# Simple keyword lists (tune these)
# --------------------------
MATH_KEYWORDS = [
    "calculate", "solve", "what is", "evaluate", "+", "-", "*", "/", "integral", "derivative",
    "sum", "subtract", "multiply", "divide", "equation", "2+2", "2 -", "find x", "simplify"
]
ENGLISH_KEYWORDS = [
    "essay", "write", "grammar", "translate", "correct", "paraphrase", "summary", "summarize",
    "proofread", "letter", "email", "story", "poem", "paragraph", "translate to", "translate from"
]

def looks_like_math(text: str) -> bool:
    t = text.lower()
    return any(k in t for k in MATH_KEYWORDS)

def looks_like_english(text: str) -> bool:
    t = text.lower()
    return any(k in t for k in ENGLISH_KEYWORDS)

# --------------------------
# Agents definitions
# --------------------------
math_agent = Agent(
    name="math_agent",
    instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
You are a helpful math assistant.
Handle math-related questions: arithmetic, algebra, geometry, trigonometry, calculus, and applied word problems.
Always show step-by-step working and give the final answer clearly.

If the request is not math-related but is about English, hand off to english_agent.
""",
    model=GEMINI_MODEL,
    handoff_description="Handles math questions."
)

english_agent = Agent(
    name="english_agent",
    instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
You are a helpful English assistant.
Handle English writing tasks: essays, grammar correction, translations, summaries, email/letter drafting, stories, proofreading.
Always return the full, direct answer (do not return a placeholder).
If the request is math-related, hand off to math_agent.
""",
    model=GEMINI_MODEL,
    handoff_description="Handles English-related tasks."
)

assistant = Agent(
    name="assistant",
    instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
You are a helpful general assistant.
- If the query is math-related (calculations, equations, numeric problems), hand off to math_agent.
- If the query is English-related (writing, grammar, translation, essays, summaries), hand off to english_agent.
- Otherwise answer directly.
Do not answer a question yourself if it clearly matches Math or English — always hand off.
""",
    model=GEMINI_MODEL,
    handoffs=[math_agent, english_agent]
)

# --------------------------
# Streamlit UI
# --------------------------
st.set_page_config(page_title="Multi-Agent Assistant", layout="centered")
st.title("🤖 Multi-Agent Assistant")
st.write("Ask anything — math, English, or general. The app will highlight which agent handled your question.")

# Status boxes (top)
col1, col2, col3 = st.columns(3)
with col1:
    general_box = st.empty()
    general_box.markdown("⬜ **General Assistant**")
with col2:
    math_box = st.empty()
    math_box.markdown("⬜ **Math Agent**")
with col3:
    english_box = st.empty()
    english_box.markdown("⬜ **English Agent**")

st.write("---")

# Input area
user_input = st.text_area("💬 Enter your question here:", height=140)
submit = st.button("Submit")

# History (optional)
if "history" not in st.session_state:
    st.session_state.history = []

def run_agent_and_get_result(starting_agent, text):
    """
    Run Runner.run in event loop safely and return result.
    """
    async def _run():
        return await Runner.run(starting_agent=starting_agent, input=text)

    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    # If loop is already running (rare in Streamlit), create a new loop in a thread
    if loop.is_running():
        # fallback: create a fresh temporary loop and run until complete
        new_loop = asyncio.new_event_loop()
        return new_loop.run_until_complete(_run())
    else:
        return loop.run_until_complete(_run())

if submit:
    if not user_input.strip():
        st.warning("Please enter a question.")
    else:
        # Reset boxes
        general_box.markdown("⬜ **General Assistant**")
        math_box.markdown("⬜ **Math Agent**")
        english_box.markdown("⬜ **English Agent**")

        # Pre-classify by keywords to force the right starting agent in case model misroutes
        if looks_like_math(user_input):
            starting_agent = math_agent
        elif looks_like_english(user_input):
            starting_agent = english_agent
        else:
            starting_agent = assistant

        with st.spinner("Thinking..."):
            try:
                result = run_agent_and_get_result(starting_agent, user_input)
            except Exception as e:
                st.error(f"Error running agents: {e}")
                result = None

        triggered = "assistant"
        # Determine triggered agent safely from result.path (best-effort)
        if result is not None:
            # result.path is often a list of AgentRunPath/Agent objects; take last name if present
            try:
                if getattr(result, "path", None):
                    last = result.path[-1]
                    # last might be an object with .name
                    triggered = getattr(last, "name", str(last)).lower()
                elif getattr(result, "final_agent", None):
                    triggered = getattr(result, "final_agent").lower()
            except Exception:
                triggered = "assistant"

        # Update UI highlight
        if "math_agent" in triggered:
            math_box.markdown("✅ **Math Agent Triggered**")
        elif "english_agent" in triggered:
            english_box.markdown("✅ **English Agent Triggered**")
        else:
            general_box.markdown("✅ **General Assistant Triggered**")

        # Extract answer text robustly
        answer = None
        if result is not None:
            answer = getattr(result, "final_output", None) \
                     or getattr(result, "final_output_text", None) \
                     or getattr(result, "output", None) \
                     or getattr(result, "result", None)

        if not answer:
            answer = "No output returned."

        # Save to history and display
        st.session_state.history.append({"agent": triggered, "input": user_input, "answer": answer})

# Show conversation history
if st.session_state.history:
    st.write("---")
    st.subheader("Conversation History")
    for i, item in enumerate(reversed(st.session_state.history), 1):
        agent_label = item["agent"]
        st.markdown(f"**{i}. Agent:** `{agent_label}`")
        st.markdown(f"**Question:** {item['input']}")
        st.markdown(f"**Answer:** {item['answer']}")
        st.write("")

