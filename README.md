# Decoding Situationship — Predicting Dating App Destinies

**WIA1006 Machine Learning · OCC 2 · Universiti Malaya**
Lecturer: Dr. Narsimlu Kemsaram

🔗 **Live App:** [machine-learning-decoding-situationship.streamlit.app](https://machine-learning-decoding-situationship.streamlit.app)

---

## About

This project applies machine learning to predict dating app relationship outcomes — **Ghosted**, **Mutual Match**, or **Catfished** — based on user behavioral patterns such as app usage, swipe ratio, messaging habits, and profile completeness.

The key innovation is the **Situationship Index**, a custom composite score (0–100) that combines app usage intensity, swipe behavior, match rate, and interaction efficiency into a single engineered feature.

---

## Dataset

- Source: [Kaggle — Dating App Behavior Dataset](https://www.kaggle.com/datasets/keyushnisar/dating-app-behavior-dataset) by keyushnisar
- Original: 50,000 records, 19 features
- After filtering: **14,974 records**, 3 balanced outcome classes

---

## Models Trained

| Rank | Model | Test Accuracy |
|------|-------|--------------|
| 1 | Random Forest (Tuned) | 34.52% |
| 2 | Logistic Regression (w/ Situationship Index) | 33.96% |
| 3 | Random Forest (Baseline) | 33.76% |
| 4 | SVM | 33.02% |
| 5 | Gradient Boosting | 32.85% |
| 6 | KNN | 32.49% |
| — | Random Baseline (3-class) | 33.33% |

All models perform near the 33.33% random baseline — expected for a synthetic dataset with limited predictive signal.

---

## App Features

- Behavioral sliders to input your own app usage patterns
- Live Situationship Index score calculation
- Real-time relationship outcome prediction
- Model comparison charts and feature importance analysis

---

## Project Structure

```
ML-Project/
├── About_Us.py               # Entry point & home page
├── pages/
│   ├── Behavioral_Pattern_Insights.py
│   ├── The_AI_Detective.py
│   ├── Model_Comparison.py
│   └── Situationship_Score_Calculator.py
├── utils/
│   └── styles.py             # Shared CSS design system
└── requirements.txt
```

---

## Setup

```bash
pip install -r requirements.txt
streamlit run About_Us.py
```

---

## Team

| Name | Role | Matric |
|------|------|--------|
| Chua Bi Yun | Data Architect | 25005610 |
| Phong Xiao Wei | Algorithm Specialist | 25005900 |
| Joyce Wong Tze Eng | ML Engineer | 25005859 |
| Choo Kah Lok | ML Engineer | 25005750 |
| Chai Xin Tong | Visual Analyst | 25005524 |
