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

st.title("📊 Class Analytics")

file = st.file_uploader("Upload CSV")

if file:
    df = pd.read_csv(file)

    numeric_cols = df.select_dtypes(include=['number']).columns
    df["Average"] = df[numeric_cols].mean(axis=1)

    st.subheader("Top 10 Students")
    st.dataframe(df.sort_values("Average", ascending=False).head(10))

    st.subheader("Low Performers")
    st.dataframe(df.sort_values("Average").head(10))

    st.subheader("Summary")
    st.metric("Class Avg", round(df["Average"].mean(), 2))

    df["Risk"] = df["Average"].apply(lambda x: "High" if x < 40 else "Medium" if x < 70 else "Low")

    st.bar_chart(df["Risk"].value_counts())