import streamlit as st
import pandas as pd

st.markdown("""
<style>

/* Remove Streamlit default UI */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* App background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #020617);
}

/* Sidebar styling */
section[data-testid="stSidebar"] {
    background: #020617;
    border-right: 1px solid #1e293b;
}

/* Sidebar text */
section[data-testid="stSidebar"] * {
    color: #cbd5f5;
}

/* Card style */
.card {
    background: rgba(30, 41, 59, 0.7);
    padding: 25px;
    border-radius: 16px;
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    box-shadow: 0 0 20px rgba(0,0,0,0.3);
    margin-bottom: 20px;
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-5px);
}

/* Buttons */
.stButton>button {
    background: linear-gradient(45deg, #22c55e, #4ade80);
    color: black;
    border-radius: 12px;
    height: 48px;
    font-weight: bold;
    border: none;
}

/* Inputs */
.stTextInput input, .stNumberInput input {
    background-color: #1e293b;
    color: white;
    border-radius: 10px;
}

/* Metrics */
[data-testid="metric-container"] {
    background: rgba(30, 41, 59, 0.8);
    padding: 15px;
    border-radius: 12px;
}

/* Titles */
h1, h2, h3 {
    color: #f8fafc;
}

</style>
""", unsafe_allow_html=True)
from datetime import date

st.set_page_config(page_title="Study Tracker", layout="wide")

st.title("📊 Study Tracker")
st.markdown("Track your daily study progress")
st.divider()


# -----------------------------
# Initialize session state
# -----------------------------
if "study_log" not in st.session_state:
    st.session_state.study_log = []

# -----------------------------
# FORM (IMPORTANT FIX)
# -----------------------------
st.subheader("➕ Add Study Record")

with st.form("study_form", clear_on_submit=True):

    col1, col2, col3 = st.columns(3)

    with col1:
        subject = st.text_input("Subject")

    with col2:
        hours = st.number_input("Hours Studied", min_value=0.0)

    with col3:
        study_date = st.date_input("Date", value=date.today())

    submit = st.form_submit_button("Add Record")

    if submit:
        if subject == "" or hours == 0:
            st.warning("Enter valid subject and hours")
        else:
            st.session_state.study_log.append({
                "Subject": subject,
                "Hours": hours,
                "Date": study_date
            })
            st.success("Study record added ✅")

# -----------------------------
# Display Logs
# -----------------------------
st.divider()
st.subheader("📋 Study History")

if len(st.session_state.study_log) == 0:
    st.info("No study records yet")
else:
    df = pd.DataFrame(st.session_state.study_log)

    st.dataframe(df, use_container_width=True)

    # Total hours
    total_hours = df["Hours"].sum()
    st.metric("⏱ Total Study Hours", total_hours)

    # Subject-wise
    st.subheader("📈 Subject-wise Study")
    subject_hours = df.groupby("Subject")["Hours"].sum()
    st.bar_chart(subject_hours)

    # Daily progress
    st.subheader("📅 Daily Progress")
    daily_hours = df.groupby("Date")["Hours"].sum()
    st.line_chart(daily_hours)

# -----------------------------
# Clear option
# -----------------------------
st.divider()

if st.button("🗑️ Clear Study Log"):
    st.session_state.study_log = []
    st.success("Study log cleared")