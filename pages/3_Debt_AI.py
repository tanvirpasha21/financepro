import streamlit as st
import pandas as pd
from domain.models import Profile
from domain.debt import months_to_freedom, insolvency_risk
from ui.charts import line_chart

st.title("Debt AI 🤖")
st.markdown("Analyze your debts and explore repayment strategies.")

# User input
profile = Profile(
    income=st.number_input("Monthly Income (£)", 0, 20000, 2800),
    fixed_expenses=st.number_input("Fixed Expenses (£)", 0, 20000, 1800),
    variable_expenses=st.number_input("Variable Expenses (£)", 0, 10000, 700),
    cash=st.number_input("Cash (£)", 0, 200000, 5000),
    debt=st.number_input("Debt (£)", 0, 500000, 12000),
    apr=st.slider("Debt APR (%)", 0.0, 60.0, 24.0),
)

monthly_payment = st.number_input("Monthly Payment (£)", 0, 50000, 300)
years = st.slider("Repayment Horizon (Years)", 1, 30, 10)

if st.button("Analyze Debt"):
    # Calculate months to repay
    months_needed = months_to_freedom(profile.debt, profile.apr, monthly_payment)
    risk = insolvency_risk(profile.debt, profile.income)
    
    # Build remaining debt and actual payments per month
    debt = profile.debt
    r = profile.apr / 100 / 12  # monthly rate
    remaining = []
    actual_payments = []

    for _ in range(years * 12):
        interest = debt * r
        pay = min(monthly_payment, debt + interest)
        debt = max(0, debt + interest - pay)
        remaining.append(debt)
        actual_payments.append(pay)
        if debt <= 0:
            break

    total_interest = sum(actual_payments) - profile.debt
    df = pd.DataFrame({"Month": range(1, len(remaining)+1), "Remaining Debt (£)": remaining})

    # Display chart
    st.subheader("Debt Repayment Over Time")
    line_chart(df, x="Month", y="Remaining Debt (£)", title="Debt Projection")

    # Display key metrics
    st.write(f"**Months to Repay:** {len(remaining)}")
    st.write(f"**Insolvency Risk:** {risk:.0%}")
    st.write(f"**Total Interest Paid:** £{total_interest:.2f}")
