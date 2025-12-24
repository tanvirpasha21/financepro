import numpy as np

def simulate_cashflow(
    months,
    start_cash,
    income,
    income_var,
    expenses,
    shock_prob,
    shock_cost,
):
    cash = start_cash
    lowest = cash

    for _ in range(months):
        inc = max(0, np.random.normal(income, income_var))
        shock = shock_cost if np.random.rand() < shock_prob else 0

        cash += inc - expenses - shock
        lowest = min(lowest, cash)

    return lowest
