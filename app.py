import streamlit as st

# --- CIGNA HEADER - ADD THIS AT THE VERY TOP ---
st.set_page_config(page_title="Respiratory QuoteFlow AI - Cigna UAE", layout="wide")

# EN | عربي Toggle (top right)
col1, col2 = st.columns([8, 2])
with col2:
    lang = st.selectbox("Language", ["EN", "عربي"], label_visibility="collapsed")
    st.caption("EN | عربي" if lang == "EN" else "عربي | EN")

# Main Title
st.title("🫁 Respiratory QuoteFlow AI")

# TRACK BADGE - Important for Ignyte!
st.markdown("""
<span style='background-color:#1E90FF; color:white; padding:6px 12px; border-radius:15px; font-weight:bold; font-size:14px;'>
TRACK: SME Quoting at Scale • Instant Quotation
</span>
""", unsafe_allow_html=True)

# INTEGRATION BADGES - Add this right after
st.markdown("""
<div style='margin-top:15px; margin-bottom:10px;'>
<span style='background-color:#1E90FF; color:white; padding:5px 10px; border-radius:12px; margin-right:8px; font-size:12px;'>✓ Salesforce CRM Ready</span>
<span style='background-color:#28a745; color:white; padding:5px 10px; border-radius:12px; margin-right:8px; font-size:12px;'>✓ Cigna Rating API Compatible</span>
<span style='background-color:#fd7e14; color:white; padding:5px 10px; border-radius:12px; font-size:12px;'>✓ Policy Admin • DHA Compliant</span>
</div>
""", unsafe_allow_html=True)

# REPO STATUS
st.success("✅ Repo: brodix-respiratory-ai | Status: Active | Respiratory Focus")
st.info("DEMO MODE — Synthetic respiratory data only. No live Cigna connection. No medical advice.")

# --- YOUR EXISTING DASHBOARD CODE STARTS HERE ---
# st.subheader("🫁 Respiratory Executive Dashboard")
# ... yung 12 Total Cases, etc. mo
