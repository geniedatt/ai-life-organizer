def generate_alerts(tasks):

    alerts = []

    overdue = [t for t in tasks if t["overdue"]]

    if len(overdue) > 3:
        alerts.append("Too many overdue tasks")

    return alerts