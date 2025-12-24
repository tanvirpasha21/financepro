def explain(profile, runway, insolvency):
    reasons = []
    actions = []

    if runway < 3:
        reasons.append("Less than 3 months of liquidity.")
        actions.append("Build emergency cash to 3–6 months.")

    if profile.fixed_expenses > profile.income * 0.6:
        reasons.append("Fixed costs dominate income.")
        actions.append("Reduce fixed costs by £200–£500.")

    if profile.apr > 25:
        reasons.append("High-interest debt compounds rapidly.")
        actions.append("Restructure or refinance high-APR debt.")

    if insolvency > 0.5:
        actions.append(
            "Current path is mathematically irrational — "
            "formal relief should be evaluated."
        )

    return reasons, actions
