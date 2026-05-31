import streamlit as st

def inject_css():
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700&display=swap');

#MainMenu, footer, header { visibility: hidden; }

.block-container {
    padding-top: 4.5rem !important;
    padding-bottom: 2rem !important;
    padding-left: 3rem !important;
    padding-right: 3rem !important;
    max-width: 100% !important;
}

.stAppViewContainer > section > div:first-child { padding-top: 0 !important; }
div[data-testid="stMarkdownContainer"] > * { margin-top: 0 !important; }
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif !important; }

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #fbeaf0 0%, #fff5f8 60%, #ffffff 100%);
    border-right: 0.5px solid #f4c0d1;
}
section[data-testid="stSidebar"] [data-testid="stSidebarNavLink"] {
    border-radius: 8px;
    margin-bottom: 2px;
    font-size: 14px;
    font-weight: 500;
    color: #5f5e5a;
}
section[data-testid="stSidebar"] [data-testid="stSidebarNavLink"]:hover {
    background: rgba(212,83,126,0.08);
    color: #993556;
}
section[data-testid="stSidebar"] [data-testid="stSidebarNavLink"][aria-current="page"] {
    background: rgba(212,83,126,0.15);
    color: #993556;
    font-weight: 700;
    border-left: 3px solid #d4537e;
}

.hero-banner {
    background: linear-gradient(135deg, #fbeaf0 0%, #e6f1fb 100%);
    border-radius: 16px;
    padding: 2.25rem 2.5rem 2rem;
    margin-bottom: 1.25rem;
    position: relative;
    overflow: hidden;
}
.hero-banner::before {
    content: '♥';
    position: absolute;
    right: 2rem; top: 0.5rem;
    font-size: 120px; opacity: 0.07;
    color: #d4537e; line-height: 1;
}
.hero-eyebrow {
    font-size: 14px; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.08em;
    color: #993556; margin-bottom: 0.5rem;
}
.hero-title {
    font-family: 'DM Serif Display', serif;
    font-size: 42px; color: #4a1528;
    line-height: 1.2; margin-bottom: 0.5rem;
}
.hero-sub {
    font-size: 18px; color: #993556;
    margin-bottom: 1.25rem; line-height: 1.6;
}
.hero-badges { display: flex; gap: 8px; flex-wrap: wrap; }
.hero-badge {
    background: rgba(212,83,126,0.12);
    color: #993556; font-size: 13px; font-weight: 600;
    padding: 5px 15px; border-radius: 20px;
}

.section-card {
    background: #ffffff;
    border: 0.5px solid rgba(0,0,0,0.12);
    border-radius: 12px;
    padding: 1.5rem 1.75rem;
    margin-bottom: 1.25rem;
}
.section-label {
    font-size: 13px; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.08em;
    color: #888780; margin-bottom: 1rem;
}

.overview-body { font-size: 17px; color: #3a3a38; line-height: 1.8; }
.overview-body strong {
    color: #993556; font-weight: 700;
    text-decoration: underline;
    text-decoration-color: rgba(212,83,126,0.35);
    text-underline-offset: 3px;
}

.badge-match { background: #eaf3de; color: #3b6d11; font-size: 13px; font-weight: 600; padding: 4px 14px; border-radius: 20px; display: inline-block; }
.badge-ghost { background: #fbeaf0; color: #993556; font-size: 13px; font-weight: 600; padding: 4px 14px; border-radius: 20px; display: inline-block; }
.badge-cat   { background: #faeeda; color: #854f0b; font-size: 13px; font-weight: 600; padding: 4px 14px; border-radius: 20px; display: inline-block; }

.info-box {
    background: #fbeaf0;
    border: 0.5px solid #f4c0d1;
    border-radius: 8px;
    padding: 0.875rem 1.25rem;
    font-size: 15px; color: #72243e; line-height: 1.5;
}
.info-box strong { font-weight: 700; }

.link-btn {
    display: inline-block; width: 100%; text-align: center;
    padding: 0.75rem 1rem; background: #d4537e;
    color: #ffffff !important; text-decoration: none !important;
    border-radius: 8px; font-size: 15px; font-weight: 700;
}
.link-btn:hover { background: #993556; color: #fff !important; }

.metric-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 12px; margin-bottom: 1.25rem; }
.metric-card {
    background: #f7f5f2;
    border: 0.5px solid rgba(0,0,0,0.1);
    border-radius: 10px;
    padding: 1rem 1.25rem;
    text-align: center;
}
.metric-val { font-size: 26px; font-weight: 700; color: #d4537e; }
.metric-lbl { font-size: 12px; color: #888780; margin-top: 3px; text-transform: uppercase; letter-spacing: 0.06em; }

.team-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; }
.member-card {
    background: #f7f5f2;
    border: 0.5px solid rgba(0,0,0,0.1);
    border-radius: 12px;
    padding: 1.25rem 1.25rem 1rem;
    display: flex; flex-direction: column; gap: 6px;
}
.member-avatar {
    width: 44px; height: 44px; border-radius: 50%;
    background: rgba(212,83,126,0.15);
    display: flex; align-items: center; justify-content: center;
    font-size: 15px; font-weight: 700; color: #993556;
    margin-bottom: 4px;
}
.member-name { font-size: 17px; font-weight: 700; color: #1a1a1a; }
.member-role { font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.06em; color: #993556; }
.member-id { font-size: 13px; color: #888780; font-family: monospace; }

.proba-row { display: flex; align-items: center; gap: 12px; margin-bottom: 10px; }
.proba-lbl { width: 110px; font-size: 14px; color: #5f5e5a; flex-shrink: 0; }
.proba-track { flex: 1; background: #f7f5f2; border-radius: 4px; height: 10px; overflow: hidden; border: 0.5px solid rgba(0,0,0,0.1); }
.proba-fill { height: 100%; border-radius: 4px; transition: width 0.4s ease; }
.proba-pct { width: 40px; text-align: right; font-size: 14px; font-weight: 700; color: #1a1a1a; }

.pink-divider { height: 1px; background: rgba(212,83,126,0.15); margin: 1.5rem 0; }

.footer-text { text-align: center; font-size: 14px; color: #888780; margin-top: 2.5rem; line-height: 1.8; }
.footer-text strong { color: #5f5e5a; font-weight: 700; }

[data-testid="stMultiSelect"] [data-baseweb="tag"] {
    background: rgba(212,83,126,0.15) !important;
    color: #993556 !important;
}
[data-testid="stExpander"] {
    border: 0.5px solid #f4c0d1 !important;
    border-radius: 8px !important;
    background: #fbeaf0 !important;
}

/* ── Sliders ── */
[data-testid="stSlider"] [data-baseweb="slider"] [role="slider"] {
    background: #d4537e !important;
    border-color: #d4537e !important;
}
[data-testid="stSlider"] [data-baseweb="slider"] [data-testid="stThumbValue"] {
    color: #993556 !important;
}
[data-testid="stSlider"] div[class*="StyledSliderTrack"] {
    background: linear-gradient(90deg, #d4537e, #f4c0d1) !important;
}

/* ── Selectbox ── */
[data-testid="stSelectbox"] [data-baseweb="select"] > div {
    border-color: #f4c0d1 !important;
    border-radius: 8px !important;
}
[data-testid="stSelectbox"] [data-baseweb="select"] > div:focus-within {
    border-color: #d4537e !important;
}

/* ── Primary button ── */
[data-testid="stButton"] > button[kind="primary"],
[data-testid="stButton"] > button {
    background: #d4537e !important;
    border: none !important;
    color: #fff !important;
    border-radius: 8px !important;
    font-weight: 700 !important;
    font-size: 15px !important;
}
[data-testid="stButton"] > button:hover {
    background: #993556 !important;
}

</style>
""", unsafe_allow_html=True)


def footer():
    st.markdown("""
<div class="footer-text">
    <strong>WIA1006 Machine Learning</strong> &nbsp;·&nbsp; Sem 2, Session 2025/2026<br>
    Dataset: Dating App Behavior Dataset (Kaggle · keyushnisar) &nbsp;·&nbsp;
    14,974 records · 3-class classification
</div>
""", unsafe_allow_html=True)


def page_header(eyebrow, title, subtitle, badges=None):
    badges_html = ""
    if badges:
        badges_html = '<div class="hero-badges">' + "".join(
            f'<span class="hero-badge">{b}</span>' for b in badges
        ) + '</div>'
    st.markdown(f"""
<div style="margin-bottom:1.5rem">
    <div style="font-size:13px;font-weight:700;text-transform:uppercase;
                letter-spacing:0.08em;color:#993556;margin-bottom:0.4rem">{eyebrow}</div>
    <div style="font-family:'DM Serif Display',serif;font-size:36px;
                color:#4a1528;line-height:1.2;margin-bottom:0.4rem">{title}</div>
    <div style="font-size:16px;color:#5f5e5a;line-height:1.6;margin-bottom:0.75rem">{subtitle}</div>
    {badges_html}
    <div style="height:2px;background:linear-gradient(90deg,#d4537e,#e6f1fb);
                border-radius:2px;margin-top:1rem"></div>
</div>
""", unsafe_allow_html=True)