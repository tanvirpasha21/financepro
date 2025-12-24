# ui/charts.py
import streamlit as st
import altair as alt
import pandas as pd

def line_chart(data: pd.DataFrame, x: str, y: str, title: str = ""):
    chart = alt.Chart(data).mark_line(point=True).encode(
        x=x,
        y=y,
        tooltip=[x, y]
    ).properties(title=title)
    st.altair_chart(chart, use_container_width=True)

