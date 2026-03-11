import sqlite3


# -----------------------------
# DATABASE CONNECTION
# -----------------------------

def get_connection():
    return sqlite3.connect("tasks.db")


# -----------------------------
# INITIALIZE DATABASE
# -----------------------------

def init_db():

    conn = get_connection()
    cursor = conn.cursor()

    # TASKS TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT,
        completed INTEGER DEFAULT 0,
        streak INTEGER DEFAULT 0,
        preferred_time TEXT DEFAULT ''
    )
    """)

    # HABITS TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS habits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        habit TEXT,
        streak INTEGER DEFAULT 0
    )
    """)

    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS memory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        note TEXT
    )
    """)


    conn.commit()
    conn.close()


# -----------------------------
# TASK FUNCTIONS
# -----------------------------

def add_task(task):

    conn = get_connection()
    cursor = conn.cursor()

    clean_task = task.strip().lower()

    cursor.execute("SELECT * FROM tasks WHERE LOWER(task)=?", (clean_task,))
    exists = cursor.fetchone()

    if not exists:
        cursor.execute("INSERT INTO tasks (task) VALUES (?)", (clean_task,))

    conn.commit()
    conn.close()


def get_tasks():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, task, completed FROM tasks")

    tasks = cursor.fetchall()

    conn.close()

    return tasks


def complete_task(task_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE tasks SET completed=1 WHERE id=?", (task_id,))

    conn.commit()
    conn.close()


def delete_task(task_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))

    conn.commit()
    conn.close()


# -----------------------------
# STREAK SYSTEM
# -----------------------------

def update_streak(task_id, preferred_time=None):

    conn = get_connection()
    cursor = conn.cursor()

    if preferred_time:
        cursor.execute(
            "UPDATE tasks SET streak = streak + 1, preferred_time=? WHERE id=?",
            (preferred_time, task_id)
        )
    else:
        cursor.execute(
            "UPDATE tasks SET streak = streak + 1 WHERE id=?",
            (task_id,)
        )

    conn.commit()
    conn.close()


def get_streak(task_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT streak FROM tasks WHERE id=?",
        (task_id,)
    )

    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]

    return 0


# -----------------------------
# HABIT FUNCTIONS
# -----------------------------

def add_habit(habit):

    conn = get_connection()
    cursor = conn.cursor()

    clean_habit = habit.strip().lower()

    cursor.execute("SELECT * FROM habits WHERE LOWER(habit)=?", (clean_habit,))
    exists = cursor.fetchone()

    if not exists:
        cursor.execute(
            "INSERT INTO habits (habit, streak) VALUES (?, 0)",
            (clean_habit,)
        )

    conn.commit()
    conn.close()


def get_habits():

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT id, habit, streak FROM habits")
        habits = cursor.fetchall()
    except sqlite3.OperationalError:
        habits = []

    conn.close()

    return habits


def save_weekly_plan(plan):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM weekly_plan")
    cursor.execute("INSERT INTO weekly_plan (plan) VALUES (?)", (plan,))

    conn.commit()
    conn.close()


def get_weekly_plan():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT plan FROM weekly_plan LIMIT 1")

    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]

    return None