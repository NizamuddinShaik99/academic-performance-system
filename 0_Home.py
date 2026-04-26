import streamlit as st

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="Academic System",
    layout="wide"
)

# ===============================
# PREMIUM CSS
# ===============================
st.markdown("""
<style>

/* Hide Streamlit elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #020617);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #020617;
}

/* Title */
.title {
    font-size: 42px;
    font-weight: bold;
    color: white;
}

/* Subtitle */
.subtitle {
    font-size: 20px;
    color: #cbd5e1;
}

/* Feature Cards */
.card {
    background: rgba(30, 41, 59, 0.8);
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    transition: 0.3s;
    box-shadow: 0 0 20px rgba(0,0,0,0.3);
}

.card:hover {
    transform: translateY(-8px);
}

/* Icons */
.icon {
    font-size: 40px;
    margin-bottom: 10px;
}

/* Text */
.card-title {
    font-size: 20px;
    font-weight: bold;
}

.card-desc {
    font-size: 14px;
    color: #94a3b8;
}

</style>
""", unsafe_allow_html=True)

# ===============================
# SIDEBAR
# ===============================
st.sidebar.title("🎓 Academic System")
st.sidebar.markdown("---")
st.sidebar.info("Navigate using sidebar")

# ===============================
# HERO SECTION
# ===============================
st.markdown('<div class="title">🎓 Academic Intelligence Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your all-in-one smart academic platform</div>', unsafe_allow_html=True)

st.markdown("---")

# ===============================
# FEATURES SECTION
# ===============================
st.markdown("### 🚀 Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <div class="icon">📊</div>
        <div class="card-title">Performance Prediction</div>
        <div class="card-desc">Predict student scores and risk level</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="icon">📈</div>
        <div class="card-title">Dashboard Analytics</div>
        <div class="card-desc">Visualize academic performance</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <div class="icon">🏫</div>
        <div class="card-title">Institution Insights</div>
        <div class="card-desc">Compare class-level performance</div>
    </div>
    """, unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("""
    <div class="card">
        <div class="icon">📅</div>
        <div class="card-title">Study Planner</div>
        <div class="card-desc">Create smart study schedules</div>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="card">
        <div class="icon">📊</div>
        <div class="card-title">Study Tracker</div>
        <div class="card-desc">Track your daily progress</div>
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown("""
    <div class="card">
        <div class="icon">🤖</div>
        <div class="card-title">Study Assistant</div>
        <div class="card-desc">Get intelligent study guidance</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ===============================
# FOOTER / CALL TO ACTION
# ===============================
st.markdown("""
### 💡 Get Started

👉 Use the sidebar to explore all features and begin your academic journey!
""")