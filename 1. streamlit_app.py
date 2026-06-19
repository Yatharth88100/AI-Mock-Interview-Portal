import streamlit as st
import random
import time

st.set_page_config(
    page_title="AI Mock Interview Portal",
    page_icon="🎤",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background-color: #0E1117;
}
.stButton>button {
    width:100%;
    border-radius:10px;
    height:3em;
}
.card {
    padding:20px;
    border-radius:15px;
    background:#1E1E1E;
    color:white;
}
</style>
""", unsafe_allow_html=True)

questions = {
    "Software Engineer": [
        "What is OOP?",
        "Difference between Stack and Queue?",
        "Explain REST API.",
        "What is a Database Index?",
        "What is Time Complexity?"
    ],
    "Data Analyst": [
        "What is Data Cleaning?",
        "Explain SQL JOIN.",
        "What is Data Visualization?",
        "Difference between Mean and Median?",
        "What is a KPI?"
    ],
    "AI/ML Engineer": [
        "What is Overfitting?",
        "Difference between AI and ML?",
        "Explain Neural Networks.",
        "What is Gradient Descent?",
        "What is Supervised Learning?"
    ]
}

st.title("🎤 AI Mock Interview Portal")

col1, col2 = st.columns([2,1])

with col1:
    role = st.selectbox(
        "Select Role",
        ["Software Engineer","Data Analyst","AI/ML Engineer"]
    )

with col2:
    difficulty = st.selectbox(
        "Difficulty",
        ["Easy","Medium","Hard"]
    )

if "question" not in st.session_state:
    st.session_state.question = ""

if st.button("Generate Question"):
    st.session_state.question = random.choice(questions[role])

if st.session_state.question:
    st.markdown("### Interview Question")
    st.info(st.session_state.question)

    answer = st.text_area(
        "Your Answer",
        height=200
    )

    if st.button("Submit Answer"):
        score = random.randint(60,95)

        st.success(f"Interview Score: {score}/100")

        if score > 85:
            st.balloons()
            st.success("Excellent Answer!")
        elif score > 70:
            st.warning("Good Answer. Add more technical depth.")
        else:
            st.error("Need Improvement.")

        st.markdown("### Feedback")
        st.write("""
        ✅ Clear Communication

        ✅ Structured Response

        ⚠ Add More Examples

        ⚠ Improve Technical Details
        """)

st.sidebar.title("📊 Dashboard")

st.sidebar.metric("Interviews Taken", random.randint(5,50))
st.sidebar.metric("Average Score", f"{random.randint(70,90)}%")
st.sidebar.metric("Confidence", f"{random.randint(60,95)}%")

st.sidebar.success("Ready for Placement Preparation 🚀")
