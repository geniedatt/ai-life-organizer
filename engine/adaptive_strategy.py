from ai.trajectory_simulator import simulate_life_trajectory


def adjust_strategy():

    trajectory = simulate_life_trajectory()

    strategy_changes = []

    life_score = trajectory["life_score"]
    momentum = trajectory["momentum"]

    # ----------------------
    # Adjust difficulty
    # ----------------------

    if life_score < 40:

        strategy_changes.append(
            "Reduce workload and focus on building daily habit stability."
        )

    elif life_score < 70:

        strategy_changes.append(
            "Maintain current goals but improve execution consistency."
        )

    else:

        strategy_changes.append(
            "Increase ambition and pursue larger strategic goals."
        )

    # ----------------------
    # Momentum adjustment
    # ----------------------

    if momentum < 40:

        strategy_changes.append(
            "Simplify your system to restore momentum."
        )

    elif momentum > 80:

        strategy_changes.append(
            "Momentum is strong. This is the best time to push major progress."
        )

    return strategy_changes


# -------------------------------------------------
# ORCHESTRATOR COMPATIBILITY FUNCTION
# -------------------------------------------------

def generate_adaptive_strategy(tasks=None, habits=None):

    strategy = adjust_strategy()

    if not strategy:
        return "No strategy adjustments needed."

    return "\n".join(strategy)