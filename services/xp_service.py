from database import get_habits, get_habit_activity


def calculate_xp():

    habits = get_habits()

    total = 0

    for habit in habits:

        habit_id = habit[0]

        activity = get_habit_activity(habit_id)

        if activity:
            total += len(activity)

    xp = total * 10

    level = xp // 100 + 1

    return xp, level