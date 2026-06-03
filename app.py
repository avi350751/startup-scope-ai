import streamlit as st
from chains import startup_chain

st.set_page_config(
    page_title="StartupScope AI",
    page_icon="🚀"
)

st.title("🚀 StartupScope AI")
st.caption("Validate startup ideas like an investor")

idea = st.text_area(
    "Startup Idea",
    height=150
)

customers = st.text_input(
    "Target Customers"
)

revenue = st.selectbox(
    "Revenue Model",
    [
        "Subscription",
        "Marketplace",
        "Ads",
        "SaaS",
        "Freemium",
        "Other"
    ]
)

if st.button("Analyze Startup"):

    if not idea:
        st.warning("Enter a startup idea.")
        st.stop()

    with st.spinner("Analyzing startup..."):

        result = startup_chain.invoke({
            "idea": idea,
            "customers": customers,
            "revenue": revenue
        })

    st.markdown(result)