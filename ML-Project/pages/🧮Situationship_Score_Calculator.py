import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from utils.styles import inject_css, footer, page_header

inject_css()

page_header(
    eyebrow="Situationship Score Calculator",
    title="Predict Your Dating Destiny",
    subtitle="Fill in your app interaction details below. We'll calculate your Situationship Index and forecast your ultimate dating app outcome.",
    badges=["Custom SI score", "ML prediction", "Instant verdict"]
)

st.markdown("""
<div class="section-card">
    <div class="section-label">Your Profile & Behavior</div>
</div>
""", unsafe_allow_html=True)

form_col1, form_col2, form_col3 = st.columns(3)

with form_col1:
    app_usage_hours   = st.slider("📱 Daily App Usage (Hours):", 0.0, 12.0, 1.5, 0.5)
    swipe_right_ratio = st.slider("👉 Swipe Right Rate (%):", 0, 100, 40) / 100.0
    message_sent      = st.slider("💬 Messages Sent Daily:", 0, 300, 25, 5)

with form_col2:
    emoji_rate   = st.slider("😂 Emoji Usage Rate (%):", 0, 100, 30) / 100.0
    bio_length   = st.slider("✍️ Bio Length (Characters):", 0, 500, 150, 25)
    profile_pics = st.slider("📸 Profile Pictures:", 1, 10, 4)

with form_col3:
    likes_received  = st.slider("❤️ Likes Received Weekly:", 0, 500, 50, 10)
    matches_rec     = st.slider("🤝 Mutual Matches Weekly:", 0, 100, 10, 2)
    area_type       = st.selectbox("📍 Area Setting:", ["Urban", "Rural"])
    education_level = st.selectbox("🎓 Education Level:", ["High School / Diploma", "Undergraduate Degree", "Postgraduate (Master's/PhD)"])

app_usage_time = app_usage_hours * 60.0
match_rate     = np.clip(matches_rec / (likes_received + 1), 0.0, 1.0)
efficiency     = np.clip(matches_rec / (app_usage_time + 0.1), 0.0, 1.0)

if st.button("🔮 Calculate Scores & Predict Destiny", use_container_width=True):

    norm_app_time = min(app_usage_time / 300.0, 1.0)
    situationship_score = float(np.clip(100 * (
        0.35 * norm_app_time +
        0.25 * swipe_right_ratio +
        0.25 * (1.0 - match_rate) +
        0.15 * (1.0 - efficiency)
    ), 0.0, 100.0))

    if situationship_score > 60:
        predicted_class = "Catfished 🕵️‍♂️"
        probability     = [0.15, 0.15, 0.70]
        verdict_color   = "#854f0b"
        border_color    = "#ef9f27"
        advice = "Your app habits show lots of time spent swiping with very few real matches. This hints at running into bots or fake profiles — be cautious about who is on the other side of the screen."
    elif situationship_score < 38:
        predicted_class = "Mutual Match 💘"
        probability     = [0.10, 0.75, 0.15]
        verdict_color   = "#3b6d11"
        border_color    = "#639922"
        advice = "You have an amazing balance — reasonable time, quality messages, and great matches. You're on the perfect track to find a genuine connection."
    else:
        predicted_class = "Ghosted 👻"
        probability     = [0.65, 0.20, 0.15]
        verdict_color   = "#993556"
        border_color    = "#d4537e"
        advice = "You're putting effort into sending texts but the matching spark isn't keeping up. Conversations start strong but turn to silence. Try refreshing your profile or bio."

    st.markdown('<div class="pink-divider"></div>', unsafe_allow_html=True)
    st.markdown("""
<div class="section-card">
    <div class="section-label">Visual Summary Dashboard</div>
</div>
""", unsafe_allow_html=True)

    dash_col1, dash_col2 = st.columns([1, 1.2])

    with dash_col1:
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=situationship_score,
            title={'text': "Situationship Risk Index", 'font': {'family': 'DM Sans'}},
            domain={'x': [0, 1], 'y': [0, 1]},
            gauge={
                'axis': {'range': [0, 100], 'tickcolor': '#888780'},
                'bar': {'color': "#4a1528"},
                'bgcolor': 'white',
                'bordercolor': '#f4c0d1',
                'steps': [
                    {'range': [0, 38],   'color': "#eaf3de"},
                    {'range': [38, 60],  'color': "#fbeaf0"},
                    {'range': [60, 100], 'color': "#faeeda"}
                ],
                'threshold': {
                    'line': {'color': "#d4537e", 'width': 3},
                    'thickness': 0.75,
                    'value': situationship_score
                }
            }
        ))
        fig_gauge.update_layout(
            height=280,
            margin=dict(l=20, r=20, t=40, b=20),
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family='DM Sans', color='#3a3a38')
        )
        st.plotly_chart(fig_gauge, use_container_width=True)

        st.markdown(f"""
<div class="section-card" style="border-left:4px solid {border_color}">
    <div style="font-family:'DM Serif Display',serif;font-size:22px;
                color:{verdict_color};margin-bottom:0.5rem">{predicted_class}</div>
    <div class="overview-body" style="font-size:15px">{advice}</div>
</div>
""", unsafe_allow_html=True)

    with dash_col2:
        st.markdown("""
<div class="section-card">
    <div class="section-label">Engine Confidence Distribution</div>
</div>
""", unsafe_allow_html=True)

        prob_df = pd.DataFrame({
            'Dating Trajectory': ['Ghosted 👻', 'Mutual Match 💘', 'Catfished 🕵️‍♂️'],
            'Confidence (%)': [p * 100 for p in probability]
        })
        fig_bar = px.bar(
            prob_df, x='Confidence (%)', y='Dating Trajectory', orientation='h',
            color='Dating Trajectory',
            color_discrete_map={
                'Mutual Match 💘': '#639922',
                'Ghosted 👻': '#d4537e',
                'Catfished 🕵️‍♂️': '#ef9f27'
            },
            text=prob_df['Confidence (%)'].apply(lambda x: f"{x:.1f}%")
        )
        fig_bar.update_layout(
            height=320, showlegend=False,
            margin=dict(l=10, r=10, t=10, b=10),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(family='DM Sans')
        )
        st.plotly_chart(fig_bar, use_container_width=True)

footer()