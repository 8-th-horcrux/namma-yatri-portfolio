
import streamlit as st

st.set_page_config(page_title="Namma Yatri Operations Analytics", layout="wide")

st.title("🚖 Namma Yatri Operations Analytics Portfolio")
st.subheader("Power BI | DAX | Business Analytics | Operations Analytics")

st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    [
        "Project Overview",
        "Executive Dashboard",
        "Revenue Analysis",
        "Zone Analysis",
        "Ride Funnel",
        "Recommendations",
        "Technical Architecture"
    ]
)

github_url = "https://github.com/8-th-horcrux/namma-yatri-operations-analytics"

if page == "Project Overview":
    st.header("Project Overview")
    st.write("""
    This project analyzes ride booking performance, revenue generation,
    ride conversion, and cancellation behavior using Power BI and DAX.
    """)
    st.markdown("""
    **Key KPIs**
    - Successful Ride Rate: 76.98%
    - Driver Cancellation Rate: 10.7%
    - Customer Cancellation Rate: 1.6%
    - Total Revenue: ₹7,51,343
    """)
    st.link_button("View GitHub Repository", github_url)

elif page == "Executive Dashboard":
    st.header("Executive Dashboard")
    st.info("Place executive_dashboard.png inside assets folder.")
    st.image("assets/executive_dashboard.png", use_container_width=True)

elif page == "Revenue Analysis":
    st.header("Revenue Analysis")
    st.image("assets/revenue_analysis_time.png", use_container_width=True)
    st.markdown("""
    ### Insights
    - Afternoon contributed the highest revenue.
    - Late night contributed the lowest revenue.
    - Revenue opportunity exists through time-slot optimization.
    """)

elif page == "Zone Analysis":
    st.header("Pickup Zone Performance")
    st.image("assets/zone_analysis.png", use_container_width=True)
    st.markdown("""
    ### Insights
    - Ramanagaram generated the highest ride requests.
    - Bangalore South generated the highest revenue.
    - High-demand zones require better driver allocation.
    """)

elif page == "Ride Funnel":
    st.header("Ride Booking Conversion Funnel")
    st.image("assets/funnel_analysis.png", use_container_width=True)
    st.metric("Ride Conversion Rate", "76.98%")
    st.metric("Opportunity Loss", "23.02%")

elif page == "Recommendations":
    st.header("Business Recommendations")
    st.markdown("""
    1. Increase driver availability during high-demand periods.
    2. Reduce driver cancellations through incentives.
    3. Improve quote-to-trip conversion.
    4. Focus operational efforts on high-performing zones.
    5. Improve demand forecasting and driver deployment.
    """)

elif page == "Technical Architecture":
    st.header("Technical Architecture")
    st.code("""
Raw Data
   ↓
Power Query
   ↓
Data Cleaning
   ↓
Data Modeling
   ↓
DAX Measures
   ↓
Power BI Dashboard
   ↓
Business Insights
""")
