import streamlit as st
import sys
import os

# ===============================
# FIX IMPORT PATH
# ===============================
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from ml.preprocess import transform_input
from ml.predict import predict_performance
from ml.explain import generate_explanation, generate_recommendations

# ===============================
# UI SETTINGS
# ===============================
st.set_page_config(page_title="Student Input", layout="wide")

st.title("📥 Student Input")

st.markdown("### Enter Academic Details")

# ===============================
# INPUTS
# ===============================
col1, col2 = st.columns(2)

with col1:
    study_hours = st.number_input("Study Hours", min_value=0.0)

with col2:
    attendance = st.slider("Attendance (%)", 0, 100)

screen_time = st.number_input("Screen Time (hrs)", min_value=0.0)
sleep_hours = st.number_input("Sleep Hours", min_value=0.0)

# ===============================
# SUBJECT INPUT
# ===============================
st.markdown("### 📚 Subject Marks")

subjects = []

num_subjects = st.number_input("Number of Subjects", min_value=1, max_value=10, step=1)

for i in range(int(num_subjects)):
    col1, col2 = st.columns(2)

    with col1:
        obtained = st.number_input(f"Subject {i+1} Marks Obtained", min_value=0.0, key=f"obt{i}")

    with col2:
        total = st.number_input(f"Subject {i+1} Total Marks", min_value=1.0, key=f"tot{i}")

    subjects.append({
        "obtained": obtained,
        "total": total
    })

# ===============================
# PREDICT BUTTON
# ===============================
if st.button("🚀 Predict"):

    data = {
        "study_hours": study_hours,
        "attendance": attendance,
        "screen_time": screen_time,
        "sleep_hours": sleep_hours,
        "subjects": subjects
    }

    # ML PROCESS
    features = transform_input(data)
    score, risk = predict_performance(features)
    reasons = generate_explanation(features)
    tips = generate_recommendations(features)

    # SAVE TO SESSION (IMPORTANT)
    st.session_state.score = score
    st.session_state.risk = risk

    # ===============================
    # OUTPUT
    # ===============================
    st.success("Prediction Generated Successfully!")

    st.write(f"### 🎯 Score: {score}")
    st.write(f"### ⚠️ Risk: {risk}")

    st.markdown("### 📌 Reasons")
    for r in reasons:
        st.write("- " + r)

    st.markdown("### 💡 Recommendations")
    for t in tips:
        st.write("- " + t)