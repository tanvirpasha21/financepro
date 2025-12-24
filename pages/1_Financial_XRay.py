import streamlit as st
from domain.models import Profile
from domain.solvency import solvency_score
from domain.debt import insolvency_risk
from domain.explain import explain

st.header("🔍 Financial X-Ray")

# Create Profile from user input
profile = Profile(
    income=st.number_input("Income (£)", 0, 20000, 2800),
    fixed_expenses=st.number_input("Fixed expenses (£)", 0, 20000, 1800),
    variable_expenses=st.number_input("Variable expenses (£)", 0, 10000, 700),
    cash=st.number_input("Cash (£)", 0, 200000, 5000),
    debt=st.number_input("Debt (£)", 0, 500000, 12000),
    apr=st.slider("Debt APR (%)", 0.0, 60.0, 24.0),
)

# Compute scores
score, runway = solvency_score(profile)
risk = insolvency_risk(profile.debt, profile.income)

# Display metrics
st.metric("Solvency Score", f"{score:.0f}/100")
st.metric("Runway (months)", f"{runway:.1f}")
st.metric("Insolvency Risk", f"{risk:.0%}")

# Explain results
reasons, actions = explain(profile, runway, risk)

st.subheader("Why this happens")
for r in reasons:
    st.write("•", r)

st.subheader("What improves this fastest")
for i, a in enumerate(actions, 1):
    st.write(f"{i}. {a}")
