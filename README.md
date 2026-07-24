# 📈 Predictive Content Engagement Engine

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-RandomForest-orange)
![SMOTE](https://img.shields.io/badge/Imbalance-SMOTE-teal)
![SHAP](https://img.shields.io/badge/Explainability-SHAP-8A2BE2)
![Status](https://img.shields.io/badge/Status-Real--data%20upgrade%20in%20progress-yellow)

Predicting whether a short-form video will achieve **high engagement ("viral")** from its features, and using SHAP to explain *which creative signals drive virality* — so content teams can optimise on evidence, not guesswork.

> **Behavioural angle:** engagement is human attention. This project models which content characteristics (hook rate, audio tempo, length) actually capture and hold it, versus vanity metrics like follower count.

---

## 📊 Results (measured on the current dataset)

| Metric | Value |
|--------|------:|
| Accuracy | 89% |
| Viral-class (1) recall | 0.75 |
| Viral-class (1) precision | 0.33 |
| Viral-class (1) F1 | 0.45 |
| Macro F1 | 0.70 |

**Honest limitation:** virality is rare (~6% of samples), so even with SMOTE the model catches most viral content (recall 0.75) but at low precision (0.33) — it raises a lot of false alarms. This is a genuine, discussable trade-off (screen many candidates to avoid missing a hit), and improving precision is the main goal of the roadmap. It is stated openly rather than papered over.

## ⚠️ Data status (honest note)
The committed notebook uses a **synthetic engagement dataset**. The repo is being upgraded to a **real public engagement dataset** where a suitable one is available, so the drivers reflect real audience behaviour.

## ⚙️ Approach
1. **Class imbalance** — **SMOTE** oversampling on the training set to counter the rare viral class.
2. **Modelling** — a **Random Forest Classifier** to capture non-linear feature interactions.
3. **Explainability** — **SHAP** ranks the creative drivers of engagement, translating the model into creative strategy.
4. **Evaluation** — full classification report with emphasis on the viral-class precision/recall trade-off.

## 🧰 Tech Stack
Python · pandas · NumPy · scikit-learn · imbalanced-learn (SMOTE) · SHAP · Matplotlib · Seaborn

---

## 📁 Repository Structure
```
├── README.md
├── requirements.txt
├── notebooks/
│   └── content_engagement_engine.ipynb
├── src/
├── data/
├── images/
└── docs/
```

## 🚀 How to Run
```bash
git clone https://github.com/kndukuba17-hub/Predictive-Content-Engagement-Engine.git
cd Predictive-Content-Engagement-Engine
pip install -r requirements.txt
jupyter notebook notebooks/content_engagement_engine.ipynb
```
Runs on Jupyter or Google Colab.

## 🗺️ Roadmap
- Move to a real engagement dataset and re-report metrics.
- Improve viral-class precision via threshold tuning and cost-sensitive learning.
- Add a precision-recall curve to make the operating-point trade-off explicit.
