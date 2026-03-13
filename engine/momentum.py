def calculate_momentum(habit_logs):

    if not habit_logs:
        return 0

    recent = habit_logs[-7:]

    completed = sum(1 for h in recent if h["completed"])

    return round((completed / len(recent)) * 100)