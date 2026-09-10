
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Executive Analytics Portfolio", page_icon="🚖", layout="wide")

THEMES = {
    "Dark Executive": {"bg":"#0E1117","text":"#FAFAFA","accent":"#4EA1FF"},
    "McKinsey Green": {"bg":"#0B1F17","text":"#F5F5F5","accent":"#00A36C"},
    "BCG Purple": {"bg":"#1B102B","text":"#FFFFFF","accent":"#8A5CF6"},
    "Power BI Gold": {"bg":"#1A1A1A","text":"#FFFFFF","accent":"#F2C811"},
    "Amazon Blue": {"bg":"#101820","text":"#FFFFFF","accent":"#00A8E1"}
}

theme = st.sidebar.selectbox("🎨 Theme", list(THEMES.keys()))
c = THEMES[theme]

st.markdown(f'''<style>
.stApp {{background-color:{c["bg"]};color:{c["text"]};}}
</style>''', unsafe_allow_html=True)

def show_image(path):
    if Path(path).exists():
        st.image(path, use_container_width=True)
    else:
        st.warning(f"Missing image: {path}")

st.title("🚖 Namma Yatri Operations Intelligence Platform")
st.caption("Executive Analytics Portfolio | Saqueib Imam")

c1,c2,c3,c4 = st.columns(4)
c1.metric("Revenue","₹7.5L")
c2.metric("Ride Success","76.98%")
c3.metric("Driver Cancel","10.7%")
c4.metric("Customer Cancel","1.6%")

tabs = st.tabs(["Executive Summary","Business Questions","Dashboards","Insights","Impact Simulator","Skills","Resources"])

with tabs[0]:
    st.header("Executive Summary")
    st.write("Business intelligence project focused on ride conversion, revenue and operational analytics.")

with tabs[1]:
    q = st.selectbox("Business Question",[
        "Highest demand zone?","Highest revenue zone?","Ride success rate?"
    ])
    if q=="Highest demand zone?":
        st.success("Ramanagaram")
    elif q=="Highest revenue zone?":
        st.success("Bangalore South")
    else:
        st.success("76.98%")

with tabs[2]:
    show_image("assets/executive_dashboard.png")
    show_image("assets/revenue_analysis_Time_Period.png")
    show_image("assets/revenue_analysis_zone.png")
    show_image("assets/ride_funnel.png")
    show_image("assets/cancellation_analysis.png")

with tabs[3]:
    st.markdown("### Key Insights\n- Driver cancellations are the primary challenge.\n- Funnel optimization can improve revenue.")

with tabs[4]:
    x = st.slider("Reduce Driver Cancellations (%)",0,20,5)
    st.metric("Estimated Extra Rides", x*10)
    st.metric("Estimated Revenue Impact", f"₹{x*7500:,}")

with tabs[5]:
    st.progress(0.95, text="Power BI 95%")
    st.progress(0.90, text="DAX 90%")
    st.progress(0.80, text="SQL 80%")

with tabs[6]:
    st.link_button("GitHub","https://github.com/8-th-horcrux/namma-yatri-operations-analytics")

st.markdown("---")
st.markdown("Built by Saqueib Imam")
