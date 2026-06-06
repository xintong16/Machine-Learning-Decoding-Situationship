import streamlit as st
import pandas as pd
import plotly.express as px
from utils.styles import inject_css, footer, page_header

inject_css()

page_header(
    eyebrow="The AI Detective",
    title="Decoding Your App Fate",
    subtitle="Our AI has analysed thousands of profiles to reveal the secret rules behind dating apps. See how your daily habits shape your destiny.",
    badges=["Habit ranking", "Fate simulator", "Tips to win"]
)

# ── Habit ranking ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-card">
    <div class="section-label">Green Flag vs. Red Flag Leaderboard</div>
    <div class="overview-body">Not all habits are equal — here is how heavily the AI weighs your daily choices.</div>
</div>
""", unsafe_allow_html=True)

importance_data = {
    "Your Dating Habits": [
        "📱 Scrolling the App for Hours",
        "👉 Swiping 'Yes' on Everyone",
        "💬 Sending Endless Texts Daily",
        "😂 Overusing Emojis in Messages",
        "📍 Living in a Rural Area",
        "🎓 Having Lower Education Level",
        "✍️ Leaving Your Bio Blank or Short",
        "💘 High Situationship Index Score",
        "📸 Uploading Lots of Profile Pictures"
    ],
    "The AI's Take": [
        "🚨 Red Flag Warning",
        "⚠️ Major Warning Sign",
        "⏳ Minor Warning Sign",
        "ℹ️ Doesn't Matter Much",
        "ℹ️ Doesn't Matter Much",
        "ℹ️ Doesn't Matter Much",
        "🛡️ Good Profile Shield",
        "🛡️ Good Profile Shield",
        "✨ Ultimate Green Flag"
    ],
    "Impact Score": [85, 65, 35, 8, 5, 3, -15, -20, -45]
}

df_importance = pd.DataFrame(importance_data)

fig_importance = px.bar(
    df_importance,
    x="Impact Score",
    y="Your Dating Habits",
    orientation="h",
    color="The AI's Take",
    color_discrete_map={
        "✨ Ultimate Green Flag": "#639922",
        "🛡️ Good Profile Shield": "#3b6d11",
        "ℹ️ Doesn't Matter Much": "#888780",
        "⏳ Minor Warning Sign": "#ef9f27",
        "⚠️ Major Warning Sign": "#ba7517",
        "🚨 Red Flag Warning": "#d4537e"
    },
    labels={"Impact Score": "Habit Power Level"},
    title="Which Habits Hurt vs. Help Your Chances"
)
fig_importance.update_layout(
    showlegend=True, height=380,
    yaxis_autorange="reversed",
    xaxis_title="← Helps You Match | Pulls You into Traps →",
    paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
    font=dict(family='DM Sans')
)
st.plotly_chart(fig_importance, use_container_width=True)

# ── Simulator ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-card">
    <div class="section-label">Predict Your App Fate</div>
    <div class="overview-body">Adjust the sliders to describe your dating style — the AI Detective will predict where that profile ends up.</div>
</div>
""", unsafe_allow_html=True)

sim_col1, sim_col2 = st.columns([1, 1.2])

with sim_col1:
    app_activity = st.select_slider(
        "⏱️ Daily Screen Time:",
        options=["Just a few minutes", "Under an hour", "A few hours", "Hours and hours!"],
        value="Under an hour"
    )
    swiping_habit = st.select_slider(
        "👉 Swiping Strategy:",
        options=["Super Picky", "Healthy Balance", "Swiping Right on Everyone"],
        value="Healthy Balance"
    )
    messaging_habit = st.select_slider(
        "💬 Messaging Style:",
        options=["Rarely replies", "Casual chatter", "Sends lots of texts"],
        value="Casual chatter"
    )
    emoji_habit = st.select_slider(
        "😂 Emoji Usage:",
        options=["Never", "Sometimes", "Every single message"],
        value="Sometimes"
    )
    bio_habit = st.select_slider(
        "✍️ Bio Quality:",
        options=["Empty / one word", "Short intro", "Detailed & thoughtful"],
        value="Short intro"
    )
    pics_habit = st.select_slider(
        "📸 Profile Pictures:",
        options=["Just 1 photo", "A few photos", "Many great photos"],
        value="A few photos"
    )
    location_habit = st.selectbox(
        "📍 Area Setting:",
        ["Urban", "Rural"]
    )
    edu_habit = st.selectbox(
        "🎓 Education Level:",
        ["High School / Diploma", "Undergraduate", "Postgraduate / PhD"]
    )

    # Score calculation
    score = 50

    if app_activity == "Just a few minutes":   score -= 20
    elif app_activity == "A few hours":        score += 15
    elif app_activity == "Hours and hours!":   score += 30

    if swiping_habit == "Super Picky":                  score -= 15
    elif swiping_habit == "Swiping Right on Everyone":  score += 25

    if messaging_habit == "Rarely replies":    score += 15
    elif messaging_habit == "Sends lots of texts": score -= 5

    if emoji_habit == "Every single message":  score += 10

    if bio_habit == "Empty / one word":        score += 20
    elif bio_habit == "Detailed & thoughtful": score -= 15

    if pics_habit == "Just 1 photo":           score += 10
    elif pics_habit == "Many great photos":    score -= 20

    if location_habit == "Rural":              score += 5

    if edu_habit == "High School / Diploma":   score += 5
    elif edu_habit == "Postgraduate / PhD":    score -= 5

with sim_col2:
    if score > 65:
        st.markdown("""
<div class="section-card" style="border-left:4px solid #d4537e">
    <div class="section-label">Detective's Verdict</div>
    <div style="font-family:'DM Serif Display',serif;font-size:22px;color:#993556;margin-bottom:0.5rem">🕵️ High Catfish & Bot Danger Zone!</div>
    <div class="overview-body">Spending hours rapidly swiping yes on everyone with a blank bio flags machine-like behaviour. Our data shows this hyperactive pattern is highly vulnerable to fake profiles and scam bots.</div>
</div>
""", unsafe_allow_html=True)
    elif score < 38:
        st.markdown("""
<div class="section-card" style="border-left:4px solid #639922">
    <div class="section-label">Detective's Verdict</div>
    <div style="font-family:'DM Serif Display',serif;font-size:22px;color:#3b6d11;margin-bottom:0.5rem">💘 Green Flags! Safe Track to a Mutual Match</div>
    <div class="overview-body">Low screen time, selective swiping, a detailed bio and great photos show true intent. The data confirms this thoughtful approach yields the highest success rate for meaningful connections.</div>
</div>
""", unsafe_allow_html=True)
    else:
        st.markdown("""
<div class="section-card" style="border-left:4px solid #ef9f27">
    <div class="section-label">Detective's Verdict</div>
    <div style="font-family:'DM Serif Display',serif;font-size:22px;color:#854f0b;margin-bottom:0.5rem">👻 The Fading Loop — High Risk of Being Ghosted</div>
    <div class="overview-body">A casual, typical user pattern. You're active enough to spark a conversation, but the habits lack the momentum needed — most connections fizzle into silence.</div>
</div>
""", unsafe_allow_html=True)

    # ── Score breakdown ───────────────────────────────────────────────────────
    score_clamped = max(0, min(100, score))
    st.markdown(f"""
<div class="section-card" style="margin-top:1rem">
    <div class="section-label">Your Situationship Risk Score</div>
    <div style="font-size:36px;font-weight:700;color:#d4537e;margin-bottom:0.5rem">{score_clamped} / 100</div>
    <div style="background:#f7f5f2;border-radius:8px;height:12px;overflow:hidden;margin-bottom:0.5rem">
        <div style="width:{score_clamped}%;height:100%;background:linear-gradient(90deg,#639922,#ef9f27,#d4537e);border-radius:8px"></div>
    </div>
    <div style="display:flex;justify-content:space-between;font-size:12px;color:#888780">
        <span>0 — Safe Match</span>
        <span>50 — Ambiguous</span>
        <span>100 — Danger Zone</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Tips ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-card">
    <div class="section-label">Tips to Success</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:0.5rem">
        <div style="background:#fbeaf0;border-radius:8px;padding:1rem 1.25rem">
            <div style="font-size:14px;font-weight:700;color:#993556;margin-bottom:0.5rem">WHAT RUINS YOUR CHANCES</div>
            <div class="overview-body" style="font-size:15px">
                <strong>Mindless app usage</strong> — leaving the app open for hours like a social feed ruins your match placement.<br><br>
                <strong>Mystery profiles</strong> — an empty bio flags you immediately as low-effort or a potential spam bot.
            </div>
        </div>
        <div style="background:#eaf3de;border-radius:8px;padding:1rem 1.25rem">
            <div style="font-size:14px;font-weight:700;color:#3b6d11;margin-bottom:0.5rem">WHAT ACTUALLY WORKS</div>
            <div class="overview-body" style="font-size:15px">
                <strong>Quality over quantity</strong> — being selective matches you with premium, active users.<br><br>
                <strong>Show yourself</strong> — more profile pictures provide natural conversation starters.
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

footer()
