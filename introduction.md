# Data-Driven Material Performance Analysis using Spectroscopic Data & Machine Learning

A complete end-to-end system for analyzing **spectroscopic signals (IR / UV-Vis / NMR)** and predicting **material performance** using **machine learning**.

This project performs:

- Signal preprocessing (baseline removal, smoothing, normalization)
- Feature extraction (peaks, statistical features, PCA)
- ML model training:
  - **Regression → Corrosion rate prediction**
  - **Classification → Material grade prediction (High / Medium / Low)**
- Model deployment via **FastAPI REST API**
- Spectral visualization for analysis

---

## 📌 **1. Project Overview**

This project converts raw spectroscopy data into meaningful predictions using data science + chemistry principles.

### **System Components**
| Layer | Description |
|-------|------------|
| **Preprocessing** | Baseline correction, Savitzky–Golay smoothing, normalization |
| **Feature Extraction** | Peak detection, PCA, mean/std/max/min stats |
| **Model Training** | Random Forest Regression + Classification |
| **Deployment** | FastAPI REST API for real-time predictions |
| **Visualization** | Matplotlib spectrum plots |



