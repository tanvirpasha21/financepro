from domain.models import NetWorthInput, DebtInput, BehaviourInput, Profile
from domain.solvency import solvency_score, calculate_runway
from domain.debt import months_to_freedom, insolvency_risk
from domain.networth import project_net_worth
from domain.explain import explain
import pandas as pd

def analyze_financial_xray(file) -> Profile:
    # For demo, let's create a dummy profile
    # In practice, parse CSV/Excel from file
    profile = Profile(
        cash=10000,
        income=3000,
        fixed_expenses=1500,
        variable_expenses=500,
        debt=8000,
        apr=12,
    )
    return profile

def project_net_worth_service(input_data: NetWorthInput) -> pd.DataFrame:
    nw_list = project_net_worth(
        months=input_data.months,
        cash=input_data.cash,
        income=input_data.income,
        expenses=input_data.expenses,
        debt=input_data.debt,
        apr=input_data.apr,
        payment=input_data.payment,
        boost=input_data.boost,
    )
    df = pd.DataFrame({"Year": range(1, len(nw_list)+1), "NetWorth": nw_list})
    return df

def debt_analysis(input_data: DebtInput) -> dict:
    months = months_to_freedom(input_data.principal, input_data.annual_interest*100, input_data.monthly_payment)
    insolvency = insolvency_risk(input_data.principal, input_data.monthly_payment*12)
    remaining = []
    debt = input_data.principal
    r = input_data.annual_interest / 12
    payment = input_data.monthly_payment
    for _ in range(input_data.years*12):
        interest = debt * r
        pay = min(payment, debt+interest)
        debt = max(0, debt+interest-pay)
        remaining.append(debt)
        if debt <= 0:
            break
    return {
        "months_to_repay": months,
        "total_interest": sum(remaining)-input_data.principal,
        "remaining_debt_over_time": remaining
    }

def behavioural_insights(input_data: BehaviourInput) -> dict:
    # Dummy profile for demo
    profile = Profile(
        cash=5000,
        income=2000,
        fixed_expenses=1200,
        variable_expenses=400,
        debt=5000,
        apr=20,
    )
    runway = calculate_runway(profile.cash, profile.fixed_expenses + profile.variable_expenses)
    insolvency = insolvency_risk(profile.debt, profile.income)
    reasons, actions = explain(profile, runway, insolvency)
    return {"Reasons": "; ".join(reasons), "Recommended Actions": "; ".join(actions)}
