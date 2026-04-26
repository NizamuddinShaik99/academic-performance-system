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
st.set_page_config(page_title="Study Planner", layout="wide")

st.title("📅 Study Planner")
st.markdown("Plan your weekly schedule")
st.divider()

# -----------------------------
# Initialize session state
# -----------------------------
if "timetable" not in st.session_state:
    st.session_state.timetable = []

# -----------------------------
# FORM (IMPORTANT FIX)
# -----------------------------
st.subheader("➕ Add Study Slot")

with st.form("planner_form", clear_on_submit=True):

    col1, col2, col3 = st.columns(3)

    with col1:
        day = st.selectbox("Day", [
            "Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"
        ])

    with col2:
        subject = st.text_input("Subject")

    with col3:
        time = st.text_input("Time (e.g., 6-7 PM)")

    submit = st.form_submit_button("Add to Timetable")

    if submit:
        if subject == "" or time == "":
            st.warning("Please enter subject and time")
        else:
            st.session_state.timetable.append({
                "Day": day,
                "Subject": subject,
                "Time": time
            })
            st.success("Added successfully ✅")

# -----------------------------
# Display Timetable
# -----------------------------
st.divider()
st.subheader("📊 Weekly Timetable")

if len(st.session_state.timetable) == 0:
    st.info("No timetable added yet")
else:
    df = pd.DataFrame(st.session_state.timetable)

    st.dataframe(df, use_container_width=True)

    # Visualization
    st.subheader("📈 Study Distribution")
    subject_count = df["Subject"].value_counts()
    st.bar_chart(subject_count)

# -----------------------------
# Clear option
# -----------------------------
st.divider()

if st.button("🗑️ Clear Timetable"):
    st.session_state.timetable = []
    st.success("Timetable cleared")