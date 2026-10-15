import streamlit as st
import pandas as pd

st.set_page_config(page_title="Respiratory QuoteFlow AI", layout="wide", page_icon="🫁")

st.markdown("## 🫁 Respiratory QuoteFlow AI")
st.caption("Smart Respiratory Risk Quotation System | Ignyte x Cigna Challenge | Repo: brodix-respiratory-ai")

st.success("✅ Repo: brodix-respiratory-ai | Status: Active | Respiratory Focus")
st.info("DEMO MODE — Synthetic respiratory data only. No live Cigna connection. No medical advice.")

st.markdown("### 🫁 Respiratory Executive Dashboard")

c1, c2, c3, c4 = st.columns(4)
with c1: st.metric("Total Cases", "12")
with c2: st.metric("Asthma Cases", "4")
with c3: st.metric("COPD Screening", "3")
with c4: st.metric("High-Risk Flagged", "2")

st.divider()

left, right = st.columns([1.2, 1])
with left:
    st.markdown("### Respiratory Quotation Pipeline")
    chart = pd.DataFrame({
        "Status": ["Asthma Mild", "COPD Risk", "Non-Smoker Clear", "Smoker Review", "Exception"],
        "Count": [4, 3, 3, 2, 2]
    })
    st.bar_chart(chart, x="Status", y="Count")

with right:
    st.markdown("### Respiratory Case Status")
    cases = pd.DataFrame({
        "Ref": ["RSP-2001", "RSP-2002", "RSP-2003", "RSP-2004"],
        "Patient": ["Asthma - Controlled", "COPD - Early", "Healthy Non-Smoker", "Smoker - 10yrs"],
        "Risk": ["Low Risk", "Medium Risk", "Very Low", "High Review"],
        "Quote": ["Instant Quote", "Under Review", "Instant Quote", "Exception"]
    })
    st.dataframe(cases, use_container_width=True, hide_index=True)

st.markdown("### 🫁 Respiratory Risk Factors")
a, b, c = st.columns(3)
with a:
    st.checkbox("Non-Smoker", value=True)
    st.checkbox("Asthma History")
with b:
    st.checkbox("COPD Family History")
    st.checkbox("Regular Exercise", value=True)
with c:
    st.slider("Years Smoking", 0, 40, 0)
    st.slider("Air Quality Exposure", 1, 10, 2)

st.markdown("### Recent Activity")
st.markdown("- ✅ RSP-2001 validated - instant quote")
st.markdown("- ⚠️ RSP-2004 flagged - smoking history")
st.markdown("- 🫁 Respiratory model loaded - synthetic demo")

st.divider()
st.caption("brodix-respiratory-ai | Respiratory Health Prototype | Not for medical use")
