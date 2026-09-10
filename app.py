import streamlit as st
import os
from pathlib import Path

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Namma Yatri Operations Analytics",
    page_icon="🚖",
    layout="wide"
)

# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.metric-card {
    background-color: #f8f9fa;
    padding: 15px;
    border-radius: 12px;
    border-left: 5px solid #1f77b4;
}

.section-header {
    color: #1f77b4;
    font-size: 32px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# IMAGE FUNCTION
# ==================================================

def show_image(path):
    if Path(path).exists():
        st.image(path, use_container_width=True)
    else:
        st.error(f"Image not found: {path}")

# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title("🚖 Namma Yatri Analytics")

page = st.sidebar.radio(
    "Navigation",
    [
        "Project Overview",
        "Executive Dashboard",
        "Revenue Analysis",
        "Zone Analysis",
        "Ride Funnel",
        "Cancellation Analysis",
        "Business Recommendations",
        "Technical Architecture"
    ]
)

# ==================================================
# HEADER
# ==================================================

st.title("🚖 Namma Yatri Operations Analytics Portfolio")

st.markdown("""
### Power BI | DAX | Business Analytics | Operations Analytics

A business intelligence project focused on:

- Ride Conversion
- Revenue Generation
- Driver & Customer Cancellations
- Operational Performance
- Demand Analysis
- Zone Performance Optimization
""")

github_url = "https://github.com/8-th-horcrux/namma-yatri-operations-analytics"

# ==================================================
# PROJECT OVERVIEW
# ==================================================

if page == "Project Overview":

    st.header("Business Problem")

    st.markdown("""
Namma Yatri wanted to understand:

- Ride demand patterns
- Revenue generation opportunities
- Ride booking conversion rates
- Driver cancellation behavior
- Customer cancellation behavior
- Zone-level performance

### Project Goal

Analyze ride booking data and provide actionable business insights
to improve operational efficiency and increase ride completion rates.
""")

    st.link_button(
        "🔗 View GitHub Repository",
        github_url
    )

    st.divider()

    st.subheader("Project Skills Demonstrated")

    st.markdown("""
✅ Power BI

✅ DAX

✅ Data Modelling

✅ KPI Development

✅ Revenue Analytics

✅ Funnel Analytics

✅ Business Intelligence

✅ Data Storytelling
""")

# ==================================================
# EXECUTIVE DASHBOARD
# ==================================================

elif page == "Executive Dashboard":

    st.header("Executive Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Revenue", "₹7,51,343")

    with col2:
        st.metric("Ride Success Rate", "76.98%")

    with col3:
        st.metric("Driver Cancellation", "10.7%")

    with col4:
        st.metric("Customer Cancellation", "1.6%")

    show_image("assets/executive_dashboard.png")

    st.markdown("""
### Executive Summary

The platform generated over ₹7.5 Lakhs in revenue while maintaining a ride success rate of nearly 77%.

Driver cancellations remain the primary operational challenge compared to customer cancellations.
""")

# ==================================================
# REVENUE ANALYSIS
# ==================================================

elif page == "Revenue Analysis":

    st.header("Time-Based Revenue Contribution Analysis")

    show_image("assets/revenue_analysis_Time_Period.png")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Revenue", "₹7,51,343")

    with col2:
        st.metric("Revenue Gap", "₹52,591")

    with col3:
        st.metric("Top Revenue Period", "Evening")

    st.markdown("""
### Key Findings

- Afternoon generated one of the strongest revenue contributions.
- Evening remained a high-performing time period.
- Late Night contributed the lowest revenue.
- Revenue contribution is distributed relatively evenly.

### Business Impact

This information can help optimize:

- Driver allocation
- Dynamic pricing
- Incentive structures
- Demand forecasting
""")

# ==================================================
# ZONE ANALYSIS
# ==================================================

elif page == "Zone Analysis":

    st.header("Pickup Zone Performance Analysis")

    show_image("assets/revenue_analysis_zone.png")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Top Pickup Zone", "Ramanagaram")

    with col2:
        st.metric("Top Revenue Zone", "Bangalore South")

    with col3:
        st.metric("Top Zone Revenue", "₹30,295")

    st.markdown("""
### Insights

#### Ramanagaram

Highest ride demand.

#### Bangalore South

Highest revenue generation.

### Recommendation

Prioritize driver allocation and operational support
for high-demand zones to maximize revenue and ride completion.
""")

# ==================================================
# RIDE FUNNEL
# ==================================================

elif page == "Ride Funnel":

    st.header("Ride Booking Conversion Funnel")

    show_image("assets/ride_funnel.png")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Ride Completion", "76.98%")

    with col2:
        st.metric("Quote Searches", "1277")

    with col3:
        st.metric("Completed Trips", "983")

    with col4:
        st.metric("Opportunity Loss", "23.02%")

    st.markdown("""
### Funnel Interpretation

Searches
↓
Quotes
↓
Driver Acceptance
↓
Completed Trips

### Business Opportunity

Reducing drop-offs between quote generation and ride completion
can significantly improve revenue.
""")

# ==================================================
# CANCELLATION ANALYSIS
# ==================================================

elif page == "Cancellation Analysis":

    st.header("Cancellation Analysis")

    show_image("assets/cancellation_analysis.png")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Driver Cancellation", "10.7%")

    with col2:
        st.metric("Customer Cancellation", "1.6%")

    st.markdown("""
### Key Findings

Driver cancellations are significantly higher than customer cancellations.

### Possible Causes

- Driver availability
- Route mismatch
- Incentive issues

### Recommended Actions

- Better route matching
- Driver incentives
- Demand prediction improvements
""")

# ==================================================
# BUSINESS RECOMMENDATIONS
# ==================================================

elif page == "Business Recommendations":

    st.header("Business Recommendations")

    show_image("assets/CARD VISUAL.png")

    st.success("""
1. Increase driver availability during peak periods.

2. Reduce driver cancellation rates through incentive programs.

3. Improve quote-to-trip conversion rates.

4. Prioritize driver deployment in high-demand zones.

5. Improve demand forecasting.

6. Improve ride completion rates through operational optimization.

7. Continuously monitor funnel performance and cancellations.
""")

# ==================================================
# TECHNICAL ARCHITECTURE
# ==================================================

elif page == "Technical Architecture":

    st.header("Technical Architecture")

    st.code("""
Raw Data
    ↓
Power Query
    ↓
Data Cleaning
    ↓
Data Modelling
    ↓
DAX Measures
    ↓
Power BI Dashboard
    ↓
Business Insights
    ↓
Business Recommendations
""")

    st.subheader("Tools Used")

    st.markdown("""
- Power BI
- DAX
- Data Modelling
- Power Query
- Business Analytics
- KPI Development
""")

    st.subheader("Skills Demonstrated")

    st.markdown("""
✅ Revenue Analytics

✅ Operational Analytics

✅ Funnel Analytics

✅ Data Storytelling

✅ Dashboard Development

✅ Business Intelligence

✅ KPI Reporting
""")

# ==================================================
# FOOTER
# ==================================================

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.link_button(
        "🔗 GitHub Repository",
        github_url
    )

with col2:
    st.link_button(
        "📄 Project Report",
        github_url
    )

st.markdown(
    "<center><b>Built by Saqueib Imam | Data Analytics Portfolio</b></center>",
    unsafe_allow_html=True
)