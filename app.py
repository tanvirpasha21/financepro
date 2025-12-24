import streamlit as st

st.set_page_config(
    page_title="Cash Shield",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- Sidebar ----------------
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

# ---------------- Home Page ----------------
st.title("Welcome to Cash Shield")
st.markdown(
    """
Cash Shield helps you take control of your financial health.  
Analyze, plan, and make smarter decisions — all in one place!
"""
)

st.markdown("---")

# ---------------- Quick Tips / CTA ----------------
st.subheader("🚀 Get Started Quickly")
st.markdown("Choose a tool below to explore your financial insights:")

# Create interactive columns
col1, col2 = st.columns(2)

with col1:
    if st.button("🔍 Financial X-Ray"):
        st.experimental_set_query_params(page="Financial_XRay")
        st.info("Go to Financial X-Ray page from the sidebar to enter your data.")

    if st.button("📈 Net Worth Futures"):
        st.experimental_set_query_params(page="Net_Worth_Futures")
        st.info("Go to Net Worth Futures page from the sidebar to simulate your wealth.")

with col2:
    if st.button("🤖 Debt AI"):
        st.experimental_set_query_params(page="Debt_AI")
        st.info("Go to Debt AI page from the sidebar to analyze debts.")

    if st.button("🧠 Behavioural AI"):
        st.experimental_set_query_params(page="Behavioural_AI")
        st.info("Go to Behavioural AI page from the sidebar to get recommendations.")

# ---------------- Interactive Info Cards ----------------
st.markdown("---")
st.subheader("💡 Why Cash Shield?")

col1, col2, col3 = st.columns(3)

col1.markdown(
    "### ✅ Plan Smarter\n"
    "Forecast net worth and cashflow to make informed decisions."
)

col2.markdown(
    "### 💰 Manage Debt\n"
    "Understand repayment timelines, interest, and risks."
)

col3.markdown(
    "### 🧠 Improve Habits\n"
    "Get actionable recommendations to improve financial behaviour."
)

# ---------------- Optional Motivational Image ----------------
st.markdown("---")
st.image(
    "https://images.unsplash.com/photo-1565372913385-0f046330bf00?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
    caption="Take control of your finances today",
    use_column_width=True
)

# ---------------- Footer ----------------
st.markdown("---")
st.markdown(
    "Made with 💙 by a personal finance enthusiast | Use responsibly for planning"
)
