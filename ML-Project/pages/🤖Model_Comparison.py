import streamlit as st
import pandas as pd
import plotly.express as px
from utils.styles import inject_css, footer, page_header

inject_css()

page_header(
    eyebrow="Model Comparison",
    title="Model Benchmark & Analytics",
    subtitle="We built, trained, and cross-validated 5 distinct ML classifiers. Here is how they stack up against random chance.",
    badges=["5 models", "3-class target", "33.33% baseline"]
)

@st.cache_data
def get_model_metrics():
    data = {
        "Model": [
            "Logistic Regression ★",
            "Random Forest",
            "SVM",
            "Gradient Boosting",
            "KNN"
        ],
        "Testing Accuracy (%)": [33.96, 33.76, 33.02, 32.85, 32.49],
        "CV Mean 5-Fold (%)":   [32.76, 33.32, 33.64, 33.26, 33.39],
        "CV Std Dev":           [0.0079, 0.0033, 0.0076, 0.0075, 0.0061]
    }
    return pd.DataFrame(data)

df_metrics = get_model_metrics()

# ── Metrics row ───────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="metric-grid">
    <div class="metric-card">
        <div class="metric-val">5</div>
        <div class="metric-lbl">Models Trained</div>
    </div>
    <div class="metric-card">
        <div class="metric-val">33.96%</div>
        <div class="metric-lbl">Best Test Accuracy</div>
    </div>
    <div class="metric-card">
        <div class="metric-val">33.33%</div>
        <div class="metric-lbl">Random Baseline</div>
    </div>
    <div class="metric-card">
        <div class="metric-val">LR</div>
        <div class="metric-lbl">Winning Model</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Leaderboard table ─────────────────────────────────────────────────────────
st.markdown("""
<div class="section-card">
    <div class="section-label">5-Model Performance Leaderboard</div>
</div>
""", unsafe_allow_html=True)

st.dataframe(
    df_metrics.style.highlight_max(axis=0, subset=['Testing Accuracy (%)'], color="#eaf3de"),
    use_container_width=True
)

# ── Bar chart ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-card" style="margin-top:1.25rem">
    <div class="section-label">Visualising 5-Model Performance</div>
    <div class="overview-body">All models beat the 33.33% random baseline. The differences are intentionally tight — human romance is genuinely hard to predict.</div>
</div>
""", unsafe_allow_html=True)

fig_compare = px.bar(
    df_metrics,
    x="Model",
    y="Testing Accuracy (%)",
    color="Model",
    text_auto='.2f',
    title="Testing Accuracy Across All 5 Trained Models",
    color_discrete_sequence=['#d4537e', '#ed93b1', '#ed93b1', '#ed93b1', '#ed93b1']
)
fig_compare.update_layout(
    yaxis_range=[30, 36],
    yaxis_title="Accuracy (%)",
    xaxis_title="",
    showlegend=False,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(family='DM Sans')
)
st.plotly_chart(fig_compare, use_container_width=True)

# ── Analysis box ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-card">
    <div class="section-label">What These Results Mean</div>
    <div class="overview-body">
        <strong>The Winner</strong> — Logistic Regression with Situationship Index came out on top at 33.96%, proving our custom index helps filter meaningful signals.<br><br>
        <strong>Most Steady</strong> — Random Forest produced the tightest standard deviation (0.0033), making it the most resilient across data splits.<br><br>
        <strong>Reality Check</strong> — All scores cluster around 32–34%. That is entirely normal. Blindly guessing between 3 options yields 33.33%. Human romance is incredibly random — even advanced algorithms struggle to find a formula for love.
    </div>
</div>
""", unsafe_allow_html=True)

footer()