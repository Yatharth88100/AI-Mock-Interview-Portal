import streamlit as st
import random

st.set_page_config(
    page_title="AI Mock Interview Portal",
    page_icon="🚀",
    layout="wide"
)

# ================= CSS =================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp{
    background: linear-gradient(
        135deg,
        #050816 0%,
        #0a0f29 40%,
        #130d35 100%
    );
}

.block-container{
    padding-top:2rem;
}

/* HERO */

.hero{
    text-align:center;
    padding:30px;
}

.gradient-title{
    font-size:64px;
    font-weight:800;
    background: linear-gradient(
        90deg,
        #00d4ff,
        #7c3aed,
        #ff00aa,
        #ff8c00
    );
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.subtitle{
    color:#d1d5db;
    font-size:20px;
    margin-top:10px;
}

/* GLASS CARD */

.card{
    background: rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.1);
    backdrop-filter: blur(12px);
    border-radius:20px;
    padding:25px;
    margin-top:15px;
    box-shadow:
        0 0 25px rgba(124,58,237,0.3);
}

/* QUESTION BOX */

.question-box{
    background: rgba(0,212,255,0.08);
    border-left:5px solid #00d4ff;
    padding:20px;
    border-radius:12px;
    color:white;
    font-size:18px;
}

/* BUTTON */

.stButton>button{
    width:100%;
    height:55px;
    border:none;
    border-radius:15px;
    color:white;
    font-size:18px;
    font-weight:700;
    background:linear-gradient(
        90deg,
        #00d4ff,
        #7c3aed,
        #ff00aa
    );
    box-shadow:0 0 20px rgba(255,0,170,.5);
}

.stButton>button:hover{
    transform:scale(1.02);
}

/* SIDEBAR */

section[data-testid="stSidebar"]{
    background:#090b1a;
}

.metric-card{
    text-align:center;
    padding:15px;
    border-radius:15px;
    background:rgba(255,255,255,0.05);
}

</style>
""", unsafe_allow_html=True)

# ================= DATA =================

questions = {
    "Software Engineer": [
        "Explain Object Oriented Programming.",
        "Difference between Stack and Queue?",
        "What is a REST API?",
        "Explain Time Complexity.",
        "What are Design Patterns?"
    ],
    "Data Analyst": [
        "What is Data Cleaning?",
        "Difference between Mean and Median?",
        "Explain SQL JOIN.",
        "What is Data Visualization?",
        "What is a KPI?"
    ],
    "AI/ML Engineer": [
        "What is Overfitting?",
        "Explain Gradient Descent.",
        "What is a Neural Network?",
        "Difference between AI and ML?",
        "What is Supervised Learning?"
    ]
}

# ================= HERO =================

st.markdown("""
<div class="hero">
    <div class="gradient-title">
        AI Mock Interview Portal 🚀
    </div>

    <div class="subtitle">
        Practice. Improve. Get Hired.
    </div>
</div>
""", unsafe_allow_html=True)

# ================= SIDEBAR =================

st.sidebar.title("📊 Performance Dashboard")

st.sidebar.metric(
    "Interviews Taken",
    random.randint(10,100)
)

st.sidebar.metric(
    "Average Score",
    f"{random.randint(70,95)}%"
)

st.sidebar.metric(
    "Confidence",
    f"{random.randint(65,99)}%"
)

st.sidebar.success("Ready for Placement Season 🚀")

# ================= CONTROLS =================

col1, col2 = st.columns(2)

with col1:
    role = st.selectbox(
        "🎯 Select Role",
        [
            "Software Engineer",
            "Data Analyst",
            "AI/ML Engineer"
        ]
    )

with col2:
    difficulty = st.selectbox(
        "⚡ Difficulty",
        [
            "Easy",
            "Medium",
            "Hard"
        ]
    )

# ================= SESSION =================

if "question" not in st.session_state:
    st.session_state.question = ""

# ================= GENERATE =================

if st.button("🎤 Generate Interview Question"):
    st.session_state.question = random.choice(
        questions[role]
    )

# ================= QUESTION =================

if st.session_state.question:

    st.markdown("""
    <div class="card">
    """, unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="question-box">
        {st.session_state.question}
        </div>
        """,
        unsafe_allow_html=True
    )

    answer = st.text_area(
        "✍️ Your Answer",
        height=220
    )

    if st.button("🚀 Submit Answer"):

        score = random.randint(65,98)

        st.markdown("### 🎯 Interview Result")

        st.progress(score/100)

        st.metric(
            "Interview Score",
            f"{score}/100"
        )

        if score >= 90:
            st.balloons()
            st.success("Outstanding Performance!")
        elif score >= 75:
            st.info("Good Answer. Add more technical depth.")
        else:
            st.warning("Needs Improvement.")

        st.markdown("### 🤖 AI Feedback")

        st.success("✅ Strong Communication")

        st.success("✅ Clear Structure")

        st.warning("⚠ Add Real-World Examples")

        st.warning("⚠ Improve Technical Details")

        st.markdown("### 📈 Hiring Probability")

        hire = min(100, score + random.randint(0,10))

        st.progress(hire/100)

        st.metric(
            "Chance of Selection",
            f"{hire}%"
        )

    st.markdown("</div>", unsafe_allow_html=True)

# ================= FOOTER =================

st.markdown("---")

st.markdown(
    "<center><h4 style='color:#9ca3af'>Built with ❤️ using Streamlit</h4></center>",
    unsafe_allow_html=True
)
