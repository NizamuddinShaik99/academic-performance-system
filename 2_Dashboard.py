import streamlit as st

# ===============================
# 🔥 PREMIUM UI CSS (ENHANCED)
# ===============================
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.stApp {
    background: linear-gradient(135deg, #0f172a, #020617);
}

/* Card Style */
.card {
    background: rgba(30, 41, 59, 0.8);
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
    box-shadow: 0 0 15px rgba(0,0,0,0.3);
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-5px);
}

/* Metric Style */
[data-testid="metric-container"] {
    background: rgba(30, 41, 59, 0.9);
    padding: 15px;
    border-radius: 12px;
}

/* Titles */
h1, h2, h3 {
    color: #f8fafc;
}

</style>
""", unsafe_allow_html=True)

# ===============================
# 🔥 CHECK DATA FROM SESSION
# ===============================
if "score" not in st.session_state:
    st.warning("⚠️ Please go to Student Input and click Predict first.")
    st.stop()

# Load data
score = st.session_state.score
risk = st.session_state.risk

# ===============================
# 🔥 DASHBOARD UI
# ===============================
st.title("📊 Dashboard")

st.markdown("### Performance Overview")

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.metric("Score", score)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.metric("Risk Level", risk)
    st.markdown('</div>', unsafe_allow_html=True)

# ===============================
# 🔥 INSIGHTS
# ===============================
st.markdown("### 📈 Insights")

st.markdown('<div class="card">', unsafe_allow_html=True)

if score < 40:
    st.error("🚨 High risk detected. Needs immediate improvement.")
elif score < 70:
    st.warning("⚠️ Moderate performance. You can improve further.")
else:
    st.success("✅ Excellent performance. Keep it up!")

st.markdown('</div>', unsafe_allow_html=True)

# ===============================
# 🔥 EXTRA: QUICK SUMMARY (NEW)
# ===============================
st.markdown("### 📌 Summary")

st.markdown('<div class="card">', unsafe_allow_html=True)

st.write(f"🎯 **Final Score:** {score}")
st.write(f"📊 **Risk Level:** {risk}")

if score < 40:
    st.write("👉 Focus more on studies and reduce distractions.")
elif score < 70:
    st.write("👉 Improve consistency and practice more.")
else:
    st.write("👉 Maintain your current performance level.")

st.markdown('</div>', unsafe_allow_html=True)