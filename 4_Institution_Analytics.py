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
import streamlit as st
import pandas as pd
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.stButton>button {
    border-radius: 12px;
    height: 50px;
    width: 100%;
    font-size: 16px;
}

.stMetric {
    background-color: #1E1E1E;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Institution Analytics", layout="wide")

st.title("🏫 Institution Analytics")
st.markdown("Analyze performance across multiple classes")

# -----------------------------
# FILE UPLOAD
# -----------------------------
file = st.file_uploader("Upload Institution CSV", type=["csv"])

if file:

    df = pd.read_csv(file)

    st.subheader("📄 Data Preview")
    st.dataframe(df.head())

    # -----------------------------
    # REQUIRED COLUMNS CHECK
    # -----------------------------
    if "Class" not in df.columns:
        st.error("CSV must contain a 'Class' column")
        st.stop()

    # -----------------------------
    # CALCULATE AVERAGE
    # -----------------------------
    numeric_cols = df.select_dtypes(include=['number']).columns
    df["Average"] = df[numeric_cols].mean(axis=1)

    # -----------------------------
    # CLASS-WISE PERFORMANCE
    # -----------------------------
    st.subheader("📊 Class-wise Performance")

    class_avg = df.groupby("Class")["Average"].mean().sort_values(ascending=False)

    st.bar_chart(class_avg)

    # -----------------------------
    # BEST & WORST CLASS
    # -----------------------------
    best_class = class_avg.idxmax()
    worst_class = class_avg.idxmin()

    col1, col2 = st.columns(2)

    with col1:
        st.success(f"🏆 Best Performing Class: {best_class}")

    with col2:
        st.error(f"📉 Lowest Performing Class: {worst_class}")

    # -----------------------------
    # RISK CLASSIFICATION
    # -----------------------------
    def classify_risk(score):
        if score < 40:
            return "High Risk"
        elif score < 70:
            return "Medium Risk"
        else:
            return "Low Risk"

    df["Risk"] = df["Average"].apply(classify_risk)

    # -----------------------------
    # RISK PER CLASS
    # -----------------------------
    st.subheader("🚨 Risk Distribution per Class")

    risk_class = df.groupby(["Class", "Risk"]).size().unstack().fillna(0)

    st.bar_chart(risk_class)

    # -----------------------------
    # TOP STUDENTS (OVERALL)
    # -----------------------------
    st.subheader("🏆 Top 10 Students")

    top_students = df.sort_values("Average", ascending=False).head(10)

    st.dataframe(top_students)

    # -----------------------------
    # LOW PERFORMERS
    # -----------------------------
    st.subheader("📉 Low Performing Students")

    low_students = df.sort_values("Average").head(10)

    st.dataframe(low_students)

    # -----------------------------
    # INSIGHTS
    # -----------------------------
    st.subheader("🔍 Insights")

    if class_avg.mean() < 50:
        st.error("Overall institution performance is low")

    elif class_avg.mean() < 70:
        st.warning("Institution performance is moderate")

    else:
        st.success("Institution performing well")

    if (df["Risk"] == "High Risk").sum() > 10:
        st.error("Large number of high-risk students detected")