import streamlit as st
import random

st.set_page_config(
page_title="Elite Interview Prep",
page_icon="🏆",
layout="wide"
)

st.markdown("""

<style>

.stApp{
    background:#0F0F0F;
}

h1,h2,h3{
    color:#F5D76E;
}

[data-testid="stSidebar"]{
    background:#121212;
}

.stButton>button{
    width:100%;
    height:55px;
    border-radius:12px;
    border:none;
    background:linear-gradient(135deg,#D4AF37,#F5D76E);
    color:black;
    font-weight:bold;
}

.card{
    background:#181818;
    padding:20px;
    border-radius:15px;
    border:1px solid #D4AF37;
}

.gold{
    color:#D4AF37;
}

.big{
    font-size:60px;
    font-weight:800;
    text-align:center;
}

.sub{
    text-align:center;
    color:#cccccc;
    font-size:20px;
}

</style>

""", unsafe_allow_html=True)

st.markdown(
"""

<div class='big'>
Elite Interview Prep 🏆
</div>

<div class='sub'>
Luxury AI-Powered Mock Interview Experience
</div>
""",
unsafe_allow_html=True
)

tab1, tab2, tab3 = st.tabs(
[
"🎤 Interview",
"📈 Analytics",
"🏅 Leaderboard"
]
)

with tab1:

```
questions = {
    "Software Engineer":[
        "What is OOP?",
        "Difference between Stack and Queue?",
        "What is REST API?"
    ],

    "AI/ML Engineer":[
        "What is Overfitting?",
        "Explain Gradient Descent.",
        "What is Supervised Learning?"
    ],

    "Data Analyst":[
        "Explain SQL JOIN.",
        "What is KPI?",
        "What is Data Cleaning?"
    ]
}

role = st.selectbox(
    "Select Role",
    list(questions.keys())
)

difficulty = st.selectbox(
    "Difficulty",
    ["Easy","Medium","Hard"]
)

if "question" not in st.session_state:
    st.session_state.question = ""

if st.button("Generate Question"):
    st.session_state.question = random.choice(
        questions[role]
    )

if st.session_state.question:

    st.info(
        st.session_state.question
    )

    answer = st.text_area(
        "Your Answer",
        height=200
    )

    if st.button("Submit Answer"):

        keywords = {

            "What is OOP?":[
                "class",
                "object",
                "inheritance",
                "polymorphism",
                "encapsulation"
            ],

            "Difference between Stack and Queue?":[
                "stack",
                "queue",
                "lifo",
                "fifo"
            ],

            "What is REST API?":[
                "api",
                "http",
                "request",
                "response",
                "server"
            ],

            "What is Overfitting?":[
                "training",
                "test",
                "model",
                "data"
            ],

            "Explain Gradient Descent.":[
                "optimization",
                "loss",
                "minimum",
                "gradient"
            ],

            "What is Supervised Learning?":[
                "label",
                "training",
                "prediction"
            ],

            "Explain SQL JOIN.":[
                "table",
                "join",
                "row",
                "column"
            ],

            "What is KPI?":[
                "performance",
                "indicator",
                "business"
            ],

            "What is Data Cleaning?":[
                "missing",
                "duplicate",
                "data"
            ]
        }

        answer_lower = answer.lower()

        current = keywords[
            st.session_state.question
        ]

        matches = 0

        for k in current:
            if k in answer_lower:
                matches += 1

        score = int(
            matches/len(current)*100
        )

        st.progress(score/100)

        st.metric(
            "Interview Score",
            f"{score}/100"
        )

        if score >= 80:
            st.success(
                "Excellent Answer 🚀"
            )

        elif score >= 50:
            st.warning(
                "Good but can improve."
            )

        else:
            st.error(
                "Needs Improvement."
            )

        missing = [
            x for x in current
            if x not in answer_lower
        ]

        st.warning(
            "Missing Concepts: "
            + ", ".join(missing)
        )
```


with tab2:

```
st.subheader("Performance Dashboard")

col1,col2,col3 = st.columns(3)

with col1:
    st.metric(
        "Interviews Taken",
        random.randint(5,50)
    )

with col2:
    st.metric(
        "Average Score",
        f"{random.randint(70,95)}%"
    )

with col3:
    st.metric(
        "Confidence",
        f"{random.randint(60,99)}%"
    )

st.progress(
    random.randint(50,95)/100
)

st.success(
    "Placement Readiness Score Generated"
)
```

with tab3:

```
st.subheader("Leaderboard")

leaderboard = [
    ("Rahul",95),
    ("Priya",91),
    ("Aman",88),
    ("Sneha",85),
    ("You",80)
]

for name,score in leaderboard:

    st.markdown(
        f"""
        🏅 {name} — {score}/100
        """
    )
```

st.markdown("---")

st.markdown(
"""

<center>
Built by Yatharth Saxena 🚀
</center>
""",
unsafe_allow_html=True
)
