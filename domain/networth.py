def project_net_worth(
    months,
    cash,
    income,
    expenses,
    debt,
    apr,
    payment,
    boost=False,
):
    r = apr / 100 / 12
    net_worth = []

    for _ in range(months):
        interest = debt * r
        effective_payment = min(
            payment * (1.4 if boost else 1.0),
            debt + interest,
        )

        debt = max(0, debt + interest - effective_payment)
        cash = cash + income - expenses - effective_payment

        net_worth.append(cash - debt)

        if cash < -5000:
            break

    return net_worth
