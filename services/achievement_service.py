from services.xp_service import calculate_xp


def get_achievements():

    xp, level = calculate_xp()

    achievements = []

    if xp >= 100:
        achievements.append("🔥 First Momentum")

    if xp >= 500:
        achievements.append("⚡ Productivity Warrior")

    if xp >= 1000:
        achievements.append("👑 Life Strategist")

    return achievements