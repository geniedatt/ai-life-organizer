import sqlite3

conn = sqlite3.connect("tasks.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT,
    completed INTEGER DEFAULT 0,
    streak INTEGER DEFAULT 0
)
""")
conn.commit()


def add_task(task):
    clean_task = task.strip().lower()

    cursor.execute("SELECT * FROM tasks WHERE LOWER(task)=?", (clean_task,))
    exists = cursor.fetchone()

    if not exists:
        cursor.execute("INSERT INTO tasks (task) VALUES (?)", (clean_task,))
        conn.commit()


def get_tasks():
    cursor.execute("SELECT id, task, completed FROM tasks")
    return cursor.fetchall()


def complete_task(task_id):
    cursor.execute("UPDATE tasks SET completed=1 WHERE id=?", (task_id,))
    conn.commit()

def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()


def update_streak(task_id):

    cursor.execute(
        "UPDATE tasks SET streak = streak + 1 WHERE id = ?",
        (task_id,)
    )

    conn.commit()

def get_streak(task_id):

    cursor.execute(
        "SELECT streak FROM tasks WHERE id = ?",
        (task_id,)
    )

    result = cursor.fetchone()

    if result:
        return result[0]

    return 0
