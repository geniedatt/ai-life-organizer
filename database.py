import sqlite3

conn = sqlite3.connect("tasks.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT,
    completed INTEGER DEFAULT 0
)
""")

conn.commit()


def add_task(task):
    cursor.execute("SELECT * FROM tasks WHERE task=?", (task,))
    exists = cursor.fetchone()

    if not exists:
        cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
        conn.commit()


def get_tasks():
    cursor.execute("SELECT * FROM tasks")
    return cursor.fetchall()


def complete_task(task_id):
    cursor.execute("UPDATE tasks SET completed=1 WHERE id=?", (task_id,))
    conn.commit()