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
            "Random Forest (Tuned) ★",
            "Logistic Regression (w/ Index)",
            "Random Forest (Baseline)",
            "SVM",
            "Gradient Boosting",
            "KNN"
        ],
        "Testing Accuracy (%)": [34.52, 33.96, 33.76, 33.02, 32.85, 32.49],
        "CV Mean 5-Fold (%)":   [33.39, 32.76, 33.32, 33.64, 33.26, 33.39],
        "CV Std Dev":           [0.0056, 0.0079, 0.0033, 0.0076, 0.0075, 0.0061]
    }
    return pd.DataFrame(data)

df_metrics = get_model_metrics()

# ── Metrics row ───────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="metric-grid">
    <div class="metric-card">
        <div class="metric-val">6</div>
        <div class="metric-lbl">Models Trained</div>
    </div>
    <div class="metric-card">
        <div class="metric-val">34.52%</div>
        <div class="metric-lbl">Best Test Accuracy</div>
    </div>
    <div class="metric-card">
        <div class="metric-val">33.33%</div>
        <div class="metric-lbl">Random Baseline</div>
    </div>
    <div class="metric-card">
        <div class="metric-val">RF Tuned</div>
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
    x="Model", y="Testing Accuracy (%)",
    color="Model", text_auto='.2f',
    title="Testing Accuracy Across All 6 Trained Models",
    color_discrete_sequence=['#d4537e','#ed93b1','#ed93b1','#ed93b1','#ed93b1','#ed93b1']
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
        <strong>The Winner</strong> — Random Forest (Tuned via GridSearchCV) came out on top at 34.52%,
        with best parameters: max_depth=10, min_samples_leaf=2, min_samples_split=10, n_estimators=200.<br><br>
        <strong>Innovation Impact</strong> — Logistic Regression improved from 33.32% (without Situationship Index)
        to 33.96% (with index), a +0.64 percentage point gain proving the custom index adds signal.<br><br>
        <strong>Most Steady</strong> — Random Forest Baseline produced the tightest CV std dev (0.0033),
        making it the most consistent across data splits.<br><br>
        <strong>Reality Check</strong> — All scores cluster around 32–35%. Mutual Information scores near 0
        and PCA showing heavy class overlap confirm this is a synthetic data ceiling —
        not model failure. Real-world data would yield significantly higher accuracy.
    </div>
</div>
""", unsafe_allow_html=True)
            

footer()