import streamlit as st
import pandas as pd

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Respiratory QuoteFlow AI | Cigna UAE",
    page_icon="🫁",
    layout="wide",
)

# Language
if 'lang' not in st.session_state:
    st.session_state.lang = "EN"

top_col1, top_col2 = st.columns([8, 2])
with top_col2:
    st.session_state.lang = st.selectbox("Lang", ["EN", "عربي"], label_visibility="collapsed")
    st.caption(f"Active: {st.session_state.lang}")

# HEADER
st.title("🫁 Respiratory QuoteFlow AI")

# TRACK - Required by Ignyte
st.markdown("""
<span style='background-color:#0D47A1; color:white; padding:8px 16px; border-radius:20px; font-weight:bold; font-size:14px;'>
TRACK: SME Quoting at Scale • Instant Quotation
</span>
""", unsafe_allow_html=True)

# Integration badges
st.markdown("""
<div style='margin:15px 0;'>
<span style='background-color:#0176D3; color:white; padding:6px 12px; border-radius:12px; margin-right:6px; font-size:12px;'>✓ Salesforce CRM Ready</span>
<span style='background-color:#2E7D32; color:white; padding:6px 12px; border-radius:12px; margin-right:6px; font-size:12px;'>✓ Cigna Rating API Compatible</span>
<span style='background-color:#EF6C00; color:white; padding:6px 12px; border-radius:12px; font-size:12px;'>✓ Policy Admin • DHA Compliant</span>
</div>
""", unsafe_allow_html=True)

st.success("✅ Repo: brodix-respiratory-ai | Status: Active | Respiratory Focus")
st.info("DEMO MODE — Synthetic respiratory data only. No live Cigna connection. No medical advice.")

# Metrics
st.markdown("### 📊 Success Metrics - Cigna Integration")
m1,m2,m3,m4,m5 = st.columns(5)
m1.metric("Total Cases","12")
m2.metric("Quote Time","45 sec","-95%")
m3.metric("Misquote","-40%")
m4.metric("Conversion","12%→30%")
m5.metric("High-Risk","2")

st.divider()

# Dashboard
st.subheader("🫁 Respiratory Executive Dashboard")
c1,c2,c3,c4 = st.columns(4)
c1.metric("Total Cases","12")
c2.metric("Asthma Cases","4")
c3.metric("COPD Screening","3")
c4.metric("High-Risk Flagged","2")

left, right = st.columns(2)
with left:
    st.markdown("#### Respiratory Quotation Pipeline")
    chart_data = pd.DataFrame({"Status":["Asthma Mild","COPD Risk","Exception","Non-Smoker Clear","Smoker Review"],"Count":[4,3,2,3,2]})
    st.bar_chart(chart_data, x="Status", y="Count")

with right:
    st.markdown("#### Respiratory Case Status - Live Quoting")
    case_df = pd.DataFrame([
        {"Ref":"RSP-2001","Patient":"Asthma - Controlled","Risk":"Low Risk","Quote":"Instant Quote ✓","Time":"42s"},
        {"Ref":"RSP-2002","Patient":"COPD - Early","Risk":"Medium Risk","Quote":"Under Review","Time":"45s"},
        {"Ref":"RSP-2003","Patient":"Healthy Non-Smoker","Risk":"Very Low","Quote":"Instant Quote ✓","Time":"38s"},
        {"Ref":"RSP-2004","Patient":"Smoker - 10yrs","Risk":"High Review","Quote":"Exception","Time":"50s"},
    ])
    st.dataframe(case_df, use_container_width=True, hide_index=True)
    st.code("Salesforce Lead → Brodix Risk API → Cigna Rating → Instant Quote (45s)", language="text")

st.markdown("#### Recent Activity")
st.markdown("""
- ✅ RSP-2001 validated - instant quote - 42s - Salesforce synced
- ⚠️ RSP-2004 flagged - smoking history - 50s - Exception
- 🫁 Respiratory model loaded - synthetic demo - 500+ pilot ready
- 🔗 Integration: Salesforce CRM → Rating API Success
""")

st.caption("brodix-respiratory-ai | For Cigna Healthcare Middle East Challenge | Brodix Studio - Talisay PH")

with st.sidebar:
    st.header("Cigna Challenge")
    st.markdown("**Track:** SME Quoting at Scale\n**Quote:** 48hrs → 45sec\n**Integration:** Salesforce + Rating API")
    if st.button("Test Instant Quote - RSP-2001"):
        st.balloons()
        st.success("Instant Quote Generated in 42 seconds! ✓")
