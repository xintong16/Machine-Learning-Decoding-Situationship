import streamlit as st
from utils.styles import inject_css, footer

st.set_page_config(
    page_title="Tying the (Data) Knot",
    page_icon="💘",
    layout="wide"
)

inject_css()   # injects all fonts, CSS, spacing globally

# ── Hero ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-banner">
    <div class="hero-eyebrow">WIA1006 Machine Learning — Group Project</div>
    <div class="hero-title">Decoding Situationship:<br>Predicting Dating App Destinies</div>
    <div class="hero-sub">Using ML to translate swipe patterns, messaging habits, and app usage into predictable relationship trajectories.</div>
    <div class="hero-badges">
        <span class="hero-badge">14,974 records</span>
        <span class="hero-badge">3-class classification</span>
        <span class="hero-badge">6 ML models</span>
        <span class="hero-badge">Situationship Index</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="info-box" style="margin-bottom:1rem">
    📱 <strong>On mobile?</strong> Tap the <strong>☰</strong> menu at the top left to navigate between pages.
</div>
""", unsafe_allow_html=True)

# ── Project Overview ──────────────────────────────────────────────────────────
st.markdown("""
<div class="section-card">
    <div class="section-label">Project Overview</div>
    <div class="overview-body">
        In this era, modern relationships highly depend on digital interactions.
        This application uses Machine Learning models to translate behaviors such as
        app usage patterns, messaging habits, and swipe behaviors into predictable
        relationship trajectories.<br><br>
        By examining interaction signals, we explored phenomena such as
        <strong>Ghosting</strong>, <strong>Catfishing</strong>, and <strong>Mutual Matches</strong>,
        giving a structural shape to the ambiguous concept of a <strong>Situationship</strong>.
    </div>
</div>
""", unsafe_allow_html=True)

# ── Project Resources ─────────────────────────────────────────────────────────
st.markdown("""
<div class="section-card">
    <div class="section-label">Project Resources</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; align-items:start">
        <a class="link-btn"
           href="https://www.kaggle.com/datasets/keyushnisar/dating-app-behavior-dataset"
           target="_blank">View source dataset on Kaggle ↗</a>
        <div class="info-box">
            💡 Use the <strong>sidebar menu</strong> to navigate across different modules of the system.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Team Members ──────────────────────────────────────────────────────────────
def initials(name):
    parts = name.split()
    return (parts[0][0] + parts[-1][0]).upper()

members = [
    ("Chua Bi Yun",        "Data Architect",       "25005610"),
    ("Phong Xiao Wei",     "Algorithm Specialist",  "25005900"),
    ("Joyce Wong Tze Eng", "ML Engineer",           "25005859"),
    ("Choo Kah Lok",       "ML Engineer",           "25005750"),
    ("Chai Xin Tong",      "Visual Analyst",        "25005524"),
]

cards_html = "".join(f"""
<div class="member-card">
    <div class="member-avatar">{initials(name)}</div>
    <div class="member-name">{name}</div>
    <div class="member-role">{role}</div>
    <div class="member-id">{uid}</div>
</div>
""" for name, role, uid in members)

cards_html += '<div class="member-card" style="opacity:0;pointer-events:none;border:none;background:transparent"></div>'

st.markdown(f"""
<div class="section-card">
    <div class="section-label">Our Team</div>
    <div class="team-grid">{cards_html}</div>
</div>
""", unsafe_allow_html=True)

footer()