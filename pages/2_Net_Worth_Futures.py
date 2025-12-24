import streamlit as st
import pandas as pd
from domain.models import Profile
from domain.networth import project_net_worth
from ui.charts import line_chart

st.title("Net Worth Futures 📈")
st.markdown("Simulate your net worth growth over time and explore different scenarios.")

# User input
profile = Profile(
    income=st.number_input("Monthly Income (£)", 0, 20000, 2800),
    fixed_expenses=st.number_input("Fixed Expenses (£)", 0, 20000, 1800),
    variable_expenses=st.number_input("Variable Expenses (£)", 0, 10000, 700),
    cash=st.number_input("Cash (£)", 0, 200000, 5000),
    debt=st.number_input("Debt (£)", 0, 500000, 12000),
    apr=st.slider("Debt APR (%)", 0.0, 60.0, 24.0),
)

payment = st.number_input("Monthly Payment (£)", 0, 50000, 300)
months = st.slider("Projection Period (Months)", 12, 360, 120)
boost = st.checkbox("Boost payments by 40%")

# Simulate net worth
if st.button("Simulate Net Worth"):
    expenses = profile.fixed_expenses + profile.variable_expenses
    nw_list = project_net_worth(
        months=months,
        cash=profile.cash,
        income=profile.income,
        expenses=expenses,
        debt=profile.debt,
        apr=profile.apr,
        payment=payment,
        boost=boost,
    )

    df = pd.DataFrame({"Month": range(1, len(nw_list)+1), "Net Worth (£)": nw_list})
    
    st.subheader("Net Worth Projection Over Time")
    line_chart(df, x="Month", y="Net Worth (£)", title="Net Worth Over Time")
    
    st.subheader("Projection Table")
    st.dataframe(df)
