import streamlit as st
import pandas as pd
import plotly.express as px
from utils.styles import inject_css, footer, page_header

inject_css()

page_header(
    eyebrow="Behavioral Pattern Insights",
    title="Online Dating Trends & Insights",
    subtitle="Explore real data patterns from thousands of app users — see how daily habits lead to matches, ghosting, or catfishing.",
    badges=["14,974 profiles", "9 behavioral features", "3 outcomes"]
)

@st.cache_data
def load_data():
    try:
        df = pd.read_csv("dating_data_final_processed.csv")
    except:
        direct_csv_url = "https://drive.google.com/uc?export=download&id=1DsmNGNKdXF6GS5_ltgNMYEpz1jcWMOMb"
        df = pd.read_csv(direct_csv_url)
    return df

try:
    df = load_data()

    target_col = 'Outcome_encoded' if 'Outcome_encoded' in df.columns else 'match_outcome'
    if target_col in df.columns:
        df['Dating Outcome'] = df[target_col].astype(str).replace({
            '0': 'Ghosted 👻', '1': 'Mutual Match 👩‍❤️‍👨', '2': 'Catfished 🕵️‍♂️',
            '0.0': 'Ghosted 👻', '1.0': 'Mutual Match 👩‍❤️‍👨', '2.0': 'Catfished 🕵️‍♂️',
            'Ghosted': 'Ghosted 👻', 'Mutual Match': 'Mutual Match 👩‍❤️‍👨', 'Catfished': 'Catfished 🕵️‍♂️'
        })
    else:
        df['Dating Outcome'] = "Unknown Status"

    friendly_names = {
        'AppUsage': 'Daily App Usage Score',
        'swipe_right_ratio': 'Swipe Right Rate (%)',
        'message_sent_count': 'Messages Sent Daily',
        'profile_pics_count': 'Profile Pictures Uploaded',
        'bio_length': 'Bio Characters Length',
        'emoji_usage_rate': 'Emoji Usage Rate',
        'Situationship_Index': 'Situationship Index'
    }

    available_cols = [c for c in friendly_names.keys() if c in df.columns]
    dropdown_labels = [friendly_names[c] for c in available_cols]

    # ── Metrics ───────────────────────────────────────────────────────────────
    most_common = df['Dating Outcome'].mode()[0] if 'Dating Outcome' in df.columns else '—'
    avg_usage = f"{df['AppUsage'].mean():.2f}" if 'AppUsage' in df.columns else '—'

    st.markdown(f"""
<div class="metric-grid">
    <div class="metric-card">
        <div class="metric-val">{len(df):,}</div>
        <div class="metric-lbl">Profiles Analyzed</div>
    </div>
    <div class="metric-card">
        <div class="metric-val">{avg_usage}</div>
        <div class="metric-lbl">Avg Daily App Usage Score</div>
    </div>
    <div class="metric-card">
        <div class="metric-val">{len(available_cols)}</div>
        <div class="metric-lbl">Behavioral Features</div>
    </div>
    <div class="metric-card">
        <div class="metric-val">3</div>
        <div class="metric-lbl">Outcome Classes</div>
    </div>
</div>
""", unsafe_allow_html=True)

    # ── Bar chart ─────────────────────────────────────────────────────────────
    if len(available_cols) >= 1:
        st.markdown("""
<div class="section-card">
    <div class="section-label">Dynamic Behavioral Profile Builder</div>
    <div class="overview-body">Build your own custom comparison chart by selecting features below.</div>
</div>
""", unsafe_allow_html=True)

        selected_labels = st.multiselect(
            "Select features to compare:",
            options=dropdown_labels,
            default=dropdown_labels[:4]
        )

        if not selected_labels:
            st.markdown('<div class="info-box">⚠️ Please select at least one feature to display the chart.</div>', unsafe_allow_html=True)
        else:
            selected_real_cols = [k for k, v in friendly_names.items() if v in selected_labels]
            df_bar_raw = df.groupby('Dating Outcome')[selected_real_cols].mean().reset_index()
            df_bar_scaled = df_bar_raw.copy()
            for col in selected_real_cols:
                col_min = df_bar_raw[col].min()
                col_max = df_bar_raw[col].max()
                df_bar_scaled[col] = (df_bar_raw[col] - col_min) / (col_max - col_min) if col_max != col_min else 0.5
            df_bar_melted = df_bar_scaled.melt(
                id_vars='Dating Outcome', value_vars=selected_real_cols,
                var_name='Habit Attribute', value_name='Relative Intensity'
            )
            df_bar_melted['Habit Label'] = df_bar_melted['Habit Attribute'].map(friendly_names)

            fig_bar = px.bar(
                df_bar_melted, y='Habit Label', x='Relative Intensity',
                color='Dating Outcome', barmode='group', orientation='h',
                title="Comparison of Habits by Outcome",
                color_discrete_map={
                    'Mutual Match 👩‍❤️‍👨': '#639922',
                    'Ghosted 👻': '#d4537e',
                    'Catfished 🕵️‍♂️': '#ef9f27'
                },
                labels={'Relative Intensity': 'Relative Intensity (Min-Max Scaled)'}
            )
            fig_bar.update_layout(
                yaxis_title="",
                height=150 + (len(selected_labels) * 80),
                xaxis=dict(showticklabels=False),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(family='DM Sans'),
                # ── Legend below chart ──
                legend=dict(
                    orientation="h",
                    yanchor="top",
                    y=-0.15,
                    xanchor="center",
                    x=0.5,
                    title=""
                )
            )
            st.plotly_chart(fig_bar, use_container_width=True)

    # ── Radar chart ───────────────────────────────────────────────────────────
    if len(available_cols) >= 3:
        st.markdown("""
<div class="section-card">
    <div class="section-label">User Behavior Profile Fingerprints</div>
    <div class="overview-body">This radar view visualizes how all habits combine simultaneously, exposing the geometric fingerprint unique to each dating destiny.</div>
</div>
""", unsafe_allow_html=True)

        df_radar_raw = df.groupby('Dating Outcome')[available_cols].mean().reset_index()
        df_radar_scaled = df_radar_raw.copy()
        for col in available_cols:
            col_min = df_radar_raw[col].min()
            col_max = df_radar_raw[col].max()
            df_radar_scaled[col] = (df_radar_raw[col] - col_min) / (col_max - col_min) if col_max != col_min else 0.5
        df_radar_melted = df_radar_scaled.melt(
            id_vars='Dating Outcome', value_vars=available_cols,
            var_name='Habit Attribute', value_name='Relative Intensity'
        )
        df_radar_melted['Habit Label'] = df_radar_melted['Habit Attribute'].map(friendly_names)

        fig_radar = px.line_polar(
            df_radar_melted, r='Relative Intensity', theta='Habit Label',
            color='Dating Outcome', line_close=True,
            title="How ML Models Separate Class Profiles",
            color_discrete_map={
                'Mutual Match 👩‍❤️‍👨': '#639922',
                'Ghosted 👻': '#d4537e',
                'Catfished 🕵️‍♂️': '#ef9f27'
            },
            template="plotly_white"
        )
        fig_radar.update_traces(fill='toself')
        fig_radar.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 1], showticklabels=False)),
            height=520,
            font=dict(family='DM Sans'),
            # ── Legend below chart ──
            legend=dict(
                orientation="h",
                yanchor="top",
                y=-0.08,
                xanchor="center",
                x=0.5,
                title=""
            )
        )
        st.plotly_chart(fig_radar, use_container_width=True)

        st.markdown("""
<div class="info-box" style="margin-bottom:2.5rem">
    💡 <strong>What this radar means:</strong> The further a colour spikes outward, the higher that group scores for that habit.
    <strong>Mutual Match (green)</strong> spikes toward app usage, messages, and profile pics.
    <strong>Catfished (amber)</strong> spikes toward Situationship Index and emoji usage.
    <strong>Ghosted (pink)</strong> spikes toward bio length but scores low on daily presence.
</div>
""", unsafe_allow_html=True)

    # ── Pie chart ─────────────────────────────────────────────────────────────
    if 'Dating Outcome' in df.columns:
        st.markdown("""
<div class="section-card" style="margin-top:3.25rem">
    <div class="section-label">Ultimate Outcome Breakdown</div>
    <div class="overview-body">What percentage of users actually get a match versus falling into dating traps?</div>
</div>
""", unsafe_allow_html=True)

        fig_pie = px.pie(
            df, names='Dating Outcome', hole=0.4, color='Dating Outcome',
            color_discrete_map={
                'Mutual Match 👩‍❤️‍👨': '#639922',
                'Ghosted 👻': '#d4537e',
                'Catfished 🕵️‍♂️': '#ef9f27'
            }
        )
        fig_pie.update_layout(
            font=dict(family='DM Sans'),
            paper_bgcolor='rgba(0,0,0,0)',
            # ── Legend below chart ──
            legend=dict(
                orientation="h",
                yanchor="top",
                y=-0.05,
                xanchor="center",
                x=0.5,
                title=""
            )
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    # ── Raw data expander ─────────────────────────────────────────────────────
    with st.expander("🔍 View sample of raw spreadsheet data"):
        display_features = [c for c in available_cols]
        if 'Dating Outcome' in df.columns:
            display_features.append('Dating Outcome')
        st.dataframe(df[display_features].head(10), use_container_width=True)

except Exception as e:
    st.markdown(
        f'<div class="info-box">🔄 <strong>Unable to load data.</strong> Error: {e}</div>',
        unsafe_allow_html=True
    )

footer()