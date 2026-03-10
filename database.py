import sqlite3
from threading import Lock

# A lock ensures only one thread writes/reads at a time
DB_LOCK = Lock()

def get_connection():
    return sqlite3.connect("tasks.db", check_same_thread=False)

# Initialize the DB once
with get_connection() as conn:
    conn.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT,
        completed INTEGER DEFAULT 0,
        streak INTEGER DEFAULT 0
    )
    """)

def add_task(task):
    clean_task = task.strip().lower()
    with DB_LOCK:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tasks WHERE LOWER(task)=?", (clean_task,))
            if not cursor.fetchone():
                cursor.execute("INSERT INTO tasks (task) VALUES (?)", (clean_task,))
                conn.commit()

def get_tasks():
    with DB_LOCK:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, task, completed FROM tasks")
            return cursor.fetchall()

def complete_task(task_id):
    with DB_LOCK:
        with get_connection() as conn:
            conn.execute("UPDATE tasks SET completed=1 WHERE id=?", (task_id,))
            conn.commit()

def delete_task(task_id):
    with DB_LOCK:
        with get_connection() as conn:
            conn.execute("DELETE FROM tasks WHERE id=?", (task_id,))
            conn.commit()

def update_streak(task_id):
    with DB_LOCK:
        with get_connection() as conn:
            conn.execute("UPDATE tasks SET streak = streak + 1 WHERE id = ?", (task_id,))
            conn.commit()

def get_streak(task_id):
    with DB_LOCK:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT streak FROM tasks WHERE id = ?", (task_id,))
            result = cursor.fetchone()
            return result[0] if result else 0
