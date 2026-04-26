import streamlit as st

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
st.set_page_config(page_title="Study Assistant", layout="wide")

st.title("📚 Study Assistant")
st.markdown("Ask anything and get guidance")
st.divider()

# -----------------------------
# USER INPUT
# -----------------------------
st.subheader("💬 Ask Assistant")

question = st.text_input("Ask anything (e.g., timetable, study plan, focus tips)")

# -----------------------------
# RESPONSE ENGINE
# -----------------------------
if st.button("Get Answer"):

    if question.strip() == "":
        st.warning("Please enter a question")
    else:
        q = question.lower()

        # -----------------------------
        # TIMETABLE
        # -----------------------------
        if "timetable" in q or "schedule" in q:

            st.subheader("📅 Study Timetable")

            st.write("• 6–7 AM → Revision")
            st.write("• 10–12 PM → Core Subjects")
            st.write("• 2–3 PM → Practice")
            st.write("• 5–6 PM → Weak Subjects")
            st.write("• 8–9 PM → Revision")

        # -----------------------------
        # IMPROVE MARKS
        # -----------------------------
        elif "improve" in q or "marks" in q:

            st.subheader("📈 Improvement Plan")

            st.write("• Study 3–4 hours daily")
            st.write("• Focus on weak subjects")
            st.write("• Revise daily")
            st.write("• Solve previous papers")
            st.write("• Maintain consistency")

        # -----------------------------
        # FOCUS
        # -----------------------------
        elif "focus" in q:

            st.subheader("🎯 Focus Tips")

            st.write("• Use Pomodoro technique")
            st.write("• Keep phone away")
            st.write("• Study in quiet place")
            st.write("• Set daily goals")

        # -----------------------------
        # STUDY PLAN
        # -----------------------------
        elif "study plan" in q or "plan" in q:

            st.subheader("📚 Study Plan")

            st.write("• Daily: 3–4 hours study")
            st.write("• Weekly: revision + test")
            st.write("• Monthly: full revision")

        # -----------------------------
        # DEFAULT
        # -----------------------------
        else:
            st.subheader("📘 General Advice")

            st.write("• Stay consistent")
            st.write("• Practice regularly")
            st.write("• Manage time well")
            st.write("• Track your progress")

# -----------------------------
# SUGGESTIONS
# -----------------------------
st.divider()
st.subheader("💡 Try asking:")

st.write("• Create a timetable")
st.write("• How to improve my marks?")
st.write("• Give me a study plan")
st.write("• How to focus?")