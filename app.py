import streamlit as st

st.set_page_config(
    page_title="Cash Shield",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar branding and navigation info
st.sidebar.title("💰 Cash Shield")
st.sidebar.markdown(
    """
Welcome to **Cash Shield** — your personal finance companion!  
Navigate using the pages below:
"""
)
st.sidebar.info(
    """
**Pages Available:**  
1. Financial X-Ray 🔍  
2. Net Worth Futures 📈  
3. Debt AI 🤖  
4. Behavioural AI 🧠
"""
)

# Home page content
st.title("Welcome to Cash Shield")
st.markdown("""
This app helps you analyze your financial health, simulate net worth growth, 
plan debt repayment, and understand your financial behaviour.  

Use the sidebar to navigate through the different tools.
""")

st.markdown("---")
st.subheader("Quick Tips:")
st.markdown("""
- Use **Financial X-Ray** to check your current financial status.  
- **Net Worth Futures** helps you forecast your wealth over time.  
- **Debt AI** provides insight into repayment strategies.  
- **Behavioural AI** gives recommendations to improve financial habits.
""")
