# secure_session_chat.py
import sqlite3
import getpass
import bcrypt
import os
from agents import Runner, SQLiteSession
from my_agent.session_agent import sess_agents
import rich
from typing import Optional

# ---------- Config ----------
DB_FILE = "conversion.db"
USERS_TABLE = "users"
SESSIONS_TABLE = "agent_sessions"
MESSAGES_TABLE = "agent_messages"

# ---------- DB / Users Setup ----------
def setup_db(db_path: str = DB_FILE):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {USERS_TABLE} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        created_at TEXT DEFAULT (datetime('now'))
    )
    """)
    conn.commit()
    conn.close()

# ---------- Auth ----------
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def check_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())

def register_user(db_path: str = DB_FILE) -> Optional[str]:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    print("\n=== Register ===")
    name = input("Enter your name: ").strip()
    username = input("Choose a username: ").strip()
    email = input("Enter your email: ").strip()

    cursor.execute(f"SELECT 1 FROM {USERS_TABLE} WHERE username = ? OR email = ?", (username, email))
    if cursor.fetchone():
        print("[❌] Username or email already exists.")
        conn.close()
        return None

    password = getpass.getpass("Choose a password: ").strip()
    password_confirm = getpass.getpass("Confirm password: ").strip()
    if password != password_confirm:
        print("[❌] Passwords do not match.")
        conn.close()
        return None

    pw_hash = hash_password(password)
    cursor.execute(
        f"INSERT INTO {USERS_TABLE} (name, username, email, password_hash) VALUES (?, ?, ?, ?)",
        (name, username, email, pw_hash)
    )
    conn.commit()
    conn.close()
    print(f"[✅] Registration successful for '{username}'.")
    return username

def login_user(db_path: str = DB_FILE) -> Optional[dict]:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    print("\n=== Login ===")
    login_id = input("Enter username or email: ").strip()
    password = getpass.getpass("Enter password: ").strip()

    cursor.execute(f"SELECT username, password_hash, name FROM {USERS_TABLE} WHERE username = ? OR email = ?",
                   (login_id, login_id))
    row = cursor.fetchone()
    conn.close()

    if not row:
        print("[❌] User not found.")
        return None

    username, pw_hash, name = row
    if check_password(password, pw_hash):
        print(f"[✅] Login successful! Welcome back, {name} ({username}).")
        return {"username": username, "name": name}
    else:
        print("[❌] Incorrect password.")
        return None

# ---------- Chat history helpers ----------
def show_user_history(username: str, db_path: str = DB_FILE):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(f"""
            SELECT role, content, created_at
            FROM {MESSAGES_TABLE}
            WHERE session_id = ?
            ORDER BY created_at ASC
        """, (username,))
        rows = cursor.fetchall()
        conn.close()

        if not rows:
            print(f"[No history found for '{username}']")
            return

        print(f"\n--- Chat History for {username} ---")
        for role, content, ts in rows:
            print(f"[{ts}] {role.capitalize()}: {content}")
        print("--- End of history ---\n")
    except sqlite3.Error as e:
        print(f"[Error reading history]: {e}")

def clear_user_history(username: str, db_path: str = DB_FILE):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {MESSAGES_TABLE} WHERE session_id = ?", (username,))
        cursor.execute(f"DELETE FROM {SESSIONS_TABLE} WHERE session_id = ?", (username,))
        conn.commit()
        conn.close()
        print(f"[✅] History cleared for '{username}'")
    except sqlite3.Error as e:
        print(f"[Error clearing history]: {e}")

# ---------- Chat loop ----------
def chat_loop(user_info: dict, db_path: str = DB_FILE):
    username = user_info["username"]
    name = user_info["name"]

    # Inject name into agent instructions
    sess_agents.instructions = f"You are a helpful assistant. The user's name is {name}. Always use their name when appropriate."

    session = SQLiteSession(
        session_id=username,
        db_path=db_path,
        sessions_table=SESSIONS_TABLE,
        messages_table=MESSAGES_TABLE
    )

    print(f"\n[Chat started for {username}]")
    print("Commands: history, clear, logout, switch, exit")

    while True:
        prompt = input(f"{username} > ").strip()

        if prompt.lower() == "logout":
            print("[Logging out...]\n")
            break
        if prompt.lower() == "switch":
            raise RuntimeError("SWITCH_USER")
        if prompt.lower() == "exit":
            raise SystemExit(0)
        if prompt.lower() == "history":
            show_user_history(username, db_path)
            continue
        if prompt.lower() == "clear":
            if input("Confirm clear (yes/no): ").strip().lower() == "yes":
                clear_user_history(username, db_path)
            continue

        try:
            result = Runner.run_sync(
                sess_agents,
                prompt,
                session=session
            )
            rich.print("[bold green]Agent Name:[/]", result.last_agent.name)
            rich.print("[bold yellow]Final Output:[/]", result.final_output)
        except Exception as e:
            print(f"[Error]: {e}")

# ---------- Main ----------
def main():
    setup_db(DB_FILE)
    print("=== Secure Multi-User Chat ===")

    current_user = None
    while True:
        try:
            if current_user is None:
                choice = input("\nChoose: (l)ogin, (r)egister, (q)uit: ").strip().lower()
                if choice == "l":
                    user_info = login_user(DB_FILE)
                    if user_info:
                        current_user = user_info
                        chat_loop(current_user, DB_FILE)
                        current_user = None
                elif choice == "r":
                    register_user(DB_FILE)
                elif choice == "q":
                    print("Goodbye.")
                    break
                else:
                    print("Type 'l', 'r', or 'q'.")
            else:
                chat_loop(current_user, DB_FILE)
                current_user = None
        except RuntimeError as e:
            if str(e) == "SWITCH_USER":
                current_user = None
            else:
                print(f"[Runtime error]: {e}")
                current_user = None
        except SystemExit:
            raise
        except Exception as ex:
            print(f"[Unexpected error]: {ex}")
            current_user = None

if __name__ == "__main__":
    main()
