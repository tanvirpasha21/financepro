import streamlit as st
from domain.models import Profile
from domain.solvency import calculate_runway, solvency_score
from domain.debt import insolvency_risk
from domain.explain import explain

st.title("Behavioural AI 🧠")
st.markdown("Understand your financial behaviour patterns and receive actionable recommendations.")

# User input
profile = Profile(
    income=st.number_input("Income (£)", 0, 20000, 2800),
    fixed_expenses=st.number_input("Fixed Expenses (£)", 0, 20000, 1800),
    variable_expenses=st.number_input("Variable Expenses (£)", 0, 10000, 700),
    cash=st.number_input("Cash (£)", 0, 200000, 5000),
    debt=st.number_input("Debt (£)", 0, 500000, 12000),
    apr=st.slider("Debt APR (%)", 0.0, 60.0, 24.0),
)

if st.button("Analyze Behaviour"):
    runway = calculate_runway(profile.cash, profile.fixed_expenses + profile.variable_expenses)
    risk = insolvency_risk(profile.debt, profile.income)
    reasons, actions = explain(profile, runway, risk)
    
    st.subheader("Why this happens")
    for r in reasons:
        st.write("•", r)

    st.subheader("Recommended Actions")
    for i, a in enumerate(actions, 1):
        st.write(f"{i}. {a}")
