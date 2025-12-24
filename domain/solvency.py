def calculate_runway(cash: float, expenses: float) -> float:
    return cash / max(1, expenses)


def solvency_score(profile) -> float:
    net_cashflow = profile.income - (
        profile.fixed_expenses + profile.variable_expenses
    )

    runway = calculate_runway(
        profile.cash,
        profile.fixed_expenses + profile.variable_expenses,
    )

    score = (
        50
        + net_cashflow / 100
        + runway * 5
        - (profile.debt / max(1, profile.income)) * 10
    )

    return max(0, min(100, score)), runway
