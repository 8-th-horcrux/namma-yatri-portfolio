import streamlit as st
import os

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Namma Yatri Operations Analytics",
    page_icon="🚖",
    layout="wide"
)

# --------------------------------------------------
# HELPER FUNCTION
# --------------------------------------------------

def show_image(path):
    if os.path.exists(path):
        st.image(path, use_container_width=True)
    else:
        st.warning(f"Image not found: {path}")

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

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

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🚖 Namma Yatri Operations Analytics Portfolio")

st.markdown("""
### Power BI | DAX | Business Analytics | Operations Analytics

A business intelligence project focused on ride conversion,
revenue generation, cancellations, and operational performance.
""")

github_url = "https://github.com/8-th-horcrux/namma-yatri-operations-analytics"

# --------------------------------------------------
# PROJECT OVERVIEW
# --------------------------------------------------

if page == "Project Overview":

    st.header("Project Overview")

    st.markdown("""
### Business Problem

Namma Yatri wanted to understand:

- Ride demand patterns
- Revenue generation
- Ride conversion funnel
- Customer cancellations
- Driver cancellations
- Zone-wise performance

### Objective

Analyze operational performance and identify opportunities
to improve ride completion rates and revenue generation.
""")

    st.link_button(
        "🔗 View GitHub Repository",
        github_url
    )

# --------------------------------------------------
# EXECUTIVE DASHBOARD
# --------------------------------------------------

elif page == "Executive Dashboard":

    st.header("Executive Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Revenue",
            "₹7,51,343"
        )

    with col2:
        st.metric(
            "Ride Success Rate",
            "76.98%"
        )

    with col3:
        st.metric(
            "Driver Cancellation",
            "10.7%"
        )

    with col4:
        st.metric(
            "Customer Cancellation",
            "1.6%"
        )

    show_image("assets/executive_dashboard.png")

    st.markdown("""
### Executive Insights

- Successful Ride Rate = 76.98%
- Driver Cancellation Rate = 10.7%
- Customer Cancellation Rate = 1.6%
- Total Revenue = ₹7.5 Lakhs

The platform demonstrates strong ride completion
performance but still has room for operational
optimization through cancellation reduction.
""")

# --------------------------------------------------
# REVENUE ANALYSIS
# --------------------------------------------------

elif page == "Revenue Analysis":

    st.header("Revenue Analysis")

    show_image("assets/revenue_analysis_time.png")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Revenue",
            "₹7,51,343"
        )

    with col2:
        st.metric(
            "Revenue Gap",
            "₹52,591"
        )

    with col3:
        st.metric(
            "Top Revenue Period",
            "Evening"
        )

    st.markdown("""
### Key Findings

- Afternoon generated the highest revenue contribution.
- Evening remained a strong revenue period.
- Late Night generated the lowest revenue.
- Revenue contribution remains relatively balanced.

### Business Impact

Understanding time-based demand helps optimize:

- Driver deployment
- Dynamic pricing
- Incentive planning
""")

# --------------------------------------------------
# ZONE ANALYSIS
# --------------------------------------------------

elif page == "Zone Analysis":

    st.header("Pickup Zone Performance Analysis")

    show_image("assets/zone_analysis.png")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Top Pickup Zone",
            "Ramanagaram"
        )

    with col2:
        st.metric(
            "Top Revenue Zone",
            "Bangalore South"
        )

    with col3:
        st.metric(
            "Top Zone Revenue",
            "₹30,295"
        )

    st.markdown("""
### Key Insights

#### Ramanagaram

Highest ride demand.

#### Bangalore South

Highest revenue generation.

### Recommendation

Allocate additional drivers to:

- Ramanagaram
- Bangalore South

to maximize ride completion and revenue.
""")

# --------------------------------------------------
# RIDE FUNNEL
# --------------------------------------------------

elif page == "Ride Funnel":

    st.header("Ride Booking Conversion Funnel")

    show_image("assets/funnel_analysis.png")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Ride Completion",
            "76.98%"
        )

    with col2:
        st.metric(
            "Quote Searches",
            "1277"
        )

    with col3:
        st.metric(
            "Completed Trips",
            "983"
        )

    with col4:
        st.metric(
            "Opportunity Loss",
            "23.02%"
        )

    st.markdown("""
### Funnel Interpretation

Searches
⬇
Quotes
⬇
Driver Acceptance
⬇
Completed Trips

### Business Insight

A significant opportunity exists between
quote generation and ride completion.

Reducing drop-offs can substantially
increase revenue.
""")

# --------------------------------------------------
# CANCELLATION ANALYSIS
# --------------------------------------------------

elif page == "Cancellation Analysis":

    st.header("Cancellation Analysis")

    show_image("assets/cancellation_analysis.png")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Driver Cancellation",
            "10.7%"
        )

    with col2:
        st.metric(
            "Customer Cancellation",
            "1.6%"
        )

    st.markdown("""
### Key Findings

Driver cancellations are significantly higher
than customer cancellations.

### Possible Causes

- Driver availability issues
- Route mismatch
- Incentive misalignment

### Suggested Actions

- Driver incentives
- Better route matching
- Demand forecasting
""")

# --------------------------------------------------
# RECOMMENDATIONS
# --------------------------------------------------

elif page == "Business Recommendations":

    st.header("Business Recommendations")

    st.success("""
1. Increase driver availability during peak periods.

2. Reduce driver cancellation rates through incentives.

3. Improve quote-to-trip conversion rates.

4. Focus driver allocation on high-demand zones.

5. Use demand forecasting to improve operational planning.

6. Increase driver engagement during evening and afternoon periods.

7. Reduce ride drop-offs through targeted operational interventions.
""")

# --------------------------------------------------
# TECHNICAL ARCHITECTURE
# --------------------------------------------------

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

    st.markdown("""
### Tools Used

- Power BI
- DAX
- Data Modelling
- Power Query
- Business Analytics

### Skills Demonstrated

- KPI Analysis
- Funnel Analysis
- Revenue Analytics
- Operational Analytics
- Data Storytelling
- Dashboard Development
""")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.markdown(
    "Built by **Saqueib Imam** | Data Analytics Portfolio"
)