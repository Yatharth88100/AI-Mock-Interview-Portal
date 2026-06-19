<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp{
    background:
    radial-gradient(circle at top right,
    rgba(212,175,55,0.15),
    transparent 25%),
    #0F0F0F;
}

.block-container{
    padding-top:2rem;
}

/* HERO */

.hero{
    text-align:center;
    padding:40px;
}

.gradient-title{
    font-size:68px;
    font-weight:800;
    background: linear-gradient(
        90deg,
        #D4AF37,
        #F5D76E,
        #FFF3B0,
        #D4AF37
    );
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.subtitle{
    color:#D6D6D6;
    font-size:22px;
    margin-top:10px;
}

/* GLASS CARD */

.card{
    background: rgba(255,255,255,0.03);
    border:1px solid rgba(212,175,55,0.25);
    backdrop-filter: blur(12px);
    border-radius:20px;
    padding:25px;
    margin-top:20px;

    box-shadow:
        0 0 30px rgba(212,175,55,0.12);
}

/* QUESTION BOX */

.question-box{
    background: rgba(212,175,55,0.08);
    border-left:5px solid #D4AF37;
    padding:20px;
    border-radius:12px;
    color:#F8F8F8;
    font-size:18px;
}

/* BUTTONS */

.stButton > button{
    width:100%;
    height:55px;

    border:none;
    border-radius:14px;

    background:
    linear-gradient(
        135deg,
        #D4AF37,
        #F5D76E
    );

    color:#111111;
    font-size:18px;
    font-weight:700;

    box-shadow:
        0 0 20px rgba(212,175,55,0.35);
}

.stButton > button:hover{
    transform:translateY(-2px);
}

/* INPUTS */

.stTextArea textarea,
.stSelectbox div[data-baseweb="select"]{
    background:#1A1A1A;
    color:white;
}

/* SIDEBAR */

section[data-testid="stSidebar"]{
    background:#121212;
    border-right:1px solid rgba(212,175,55,0.2);
}

/* METRICS */

[data-testid="metric-container"]{
    background:#181818;
    border:1px solid rgba(212,175,55,0.15);
    border-radius:15px;
    padding:15px;
}

/* FOOTER */

.footer{
    text-align:center;
    color:#A3A3A3;
    margin-top:20px;
}

</style>
