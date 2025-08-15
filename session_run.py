

# ! session_run.py
import asyncio
from agents import Runner,SQLiteSession
from my_agent.session_agent import sess_agents
import rich

session = SQLiteSession("user_1",'conversion.db')

async def main():
    user_data = await session.get_items()
    for user in user_data:
        rich.print(f"{user['role']}:{user['content']}")
    # rich.print(user_data)


asyncio.run(main())



# ! session_run.py
# import asyncio
# from agents import SQLiteSession
# from rich.console import Console
# from rich.text import Text

# console = Console()
# session = SQLiteSession("user_1", 'conversion.db')

# async def main():
#     user_data = await session.get_items()
#     for item in user_data:
#         role = item.get('role', 'user')
#         content = item.get('content', '')

#         # Agar assistant ka response nested list/dict hai
#         if role == 'assistant' and isinstance(content, list):
#             # Extract only 'text' from each element
#             texts = [c.get('text', '') for c in content if isinstance(c, dict)]
#             content = ' '.join(texts)

#         # Create colored text
#         if role == 'user':
#             t = Text(f"{role}: {content}", style="bold blue")
#         else:
#             t = Text(f"{role}: {content}\n\n", style="bold green")

#         console.print(t)

# asyncio.run(main())



# # while True:
# #     prompt = input("Write prompt here: ")
    
# #     if prompt == "exit":
# #         break
    
# #     result = Runner.run_sync(
# #         sess_agents, 
# #         prompt,
# #         session=session
# #         )

# #     rich.print("[bold green]Agent Name:[/]", result.last_agent.name)
# #     rich.print("[bold yellow]Final Output:[/]", result.final_output)



# import asyncio
# from agents import Runner, SQLiteSession
# from my_agent.session_agent import sess_agents
# import rich

# # Persistent session for user_1
# session = SQLiteSession("user_1", "conversion.db")

# while True:
#     prompt = input("Write prompt here (type 'exit', 'history', 'undo', 'clear'): ")

#     if prompt.lower() == "exit":
#         break

#     elif prompt.lower() == "history":
#         # Async call to get all session items
#         items = asyncio.run(session.get_items())
#         rich.print("[bold cyan]--- Conversation History ---[/]")
#         if not items:
#             rich.print("[italic]No history yet[/]")
#         for item in items:
#             role = item.get("role", "user")
#             # Optional: add username if stored in session
#             username = item.get("username", "")
#             if username:
#                 rich.print(f"[{role} | {username}] {item['content']}")
#             else:
#                 rich.print(f"[{role}] {item['content']}")
#         continue

#     elif prompt.lower() == "undo":
#         # Remove last two items: assistant + user input
#         try:
#             last_assistant = asyncio.run(session.pop_item())
#             last_user = asyncio.run(session.pop_item())
#             rich.print(f"[bold red]Removed last user input and agent response:[/]")
#             rich.print(f"User: {last_user}")
#             rich.print(f"Assistant: {last_assistant}")
#         except Exception:
#             rich.print("[bold red]Nothing to undo[/]")
#         continue

#     elif prompt.lower() == "clear":
#         asyncio.run(session.clear_session())
#         rich.print("[bold red]Session cleared![/]")
#         continue

#     # Normal conversation flow
#     result = Runner.run_sync(
#         sess_agents,
#         prompt,
#         session=session
#     )

#     rich.print("[bold green]Agent Name:[/]", result.last_agent.name)
#     rich.print("[bold yellow]Final Output:[/]", result.final_output)

