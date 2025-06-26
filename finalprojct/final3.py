import streamlit as st

# Page configuration
st.set_page_config(page_title="Homepage", layout="wide")

# --- CUSTOM CSS FOR PROFESSIONAL GRADIENT BACKGROUND & STYLING ---
st.markdown("""
    <style>
        /* Apply a clean, subtle background */
        .stApp {
            background: linear-gradient(to right, #f0f4f8, #d9e2ec);
            color: #2c3e50;
            font-family: 'Segoe UI', sans-serif;
            padding: 2rem;
        }

        /* Title styling */
        .title {
            font-size: 44px;
            font-weight: bold;
            color: #2c3e50;
            text-align: center;
            margin-top: 30px;
        }

        /* Subtitle styling */
        .subtitle {
            font-size: 20px;
            color: #4a4a4a;
            text-align: center;
            margin-bottom: 50px;
        }

        /* Button styling */
        .stButton > button {
            font-size: 16px;
            padding: 14px 28px;
            width: 100%;
            background-color: #4a90e2;
            color: white;
            border: none;
            border-radius: 10px;
            box-shadow: 1px 1px 6px rgba(0,0,0,0.1);
            transition: all 0.3s ease-in-out;
        }

        .stButton > button:hover {
            background-color: #3b73c6;
            transform: translateY(-2px);
        }
    </style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown('<div class="title">AQI Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Select a place to view predicted air quality levels</div>', unsafe_allow_html=True)

# --- LOCATION BUTTONS ---
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📍 Karyavattom"):
        st.switch_page("pages/project.py")

with col2:
    if st.button("📍 Kollam"):
        st.switch_page("pages/kollam.py")

with col3:
    if st.button("📍 Eloor"):
        st.switch_page("pages/eloor.py")

