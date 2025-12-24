import math

def months_to_freedom(debt, apr, payment):
    if debt <= 0 or payment <= 0:
        return 0
    r = apr / 100 / 12
    if payment <= debt * r:
        return math.inf
    return math.log(payment / (payment - debt * r)) / math.log(1 + r)


def insolvency_risk(debt, income):
    return min(0.9, (debt / max(1, income)) * 0.15)
