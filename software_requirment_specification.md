# 📝 Software Requirements Specification (SRS)
## Project: Data-Driven Material Performance Analysis using Spectroscopic Data & Machine Learning  
### Version 1.0  
### Prepared by: Sourav Kumar Hazra

---

# 1. Introduction

## 1.1 Purpose
The purpose of this project is to build a **machine learning-driven system** that processes **spectroscopic data** (IR, UV-Vis, NMR) to:

- Predict **corrosion resistance** (regression)
- Classify **material grade**: High / Medium / Low (classification)
- Provide predictions via a **FastAPI-based REST API**
- Support real-world datasets collected from spectroscopy sensors

This SRS defines functional, non-functional, and dataset requirements.

---

# 2. Overall Description

## 2.1 Product Perspective
The system is composed of:

- Data Preprocessing Layer  
- Feature Extraction Engine  
- Machine Learning Models  
- API Integration Layer  
- Visualization Support

It is standalone and deployable locally or on cloud.

## 2.2 Product Features
- Baseline correction  
- Smoothing & noise reduction  
- Peak detection  
- PCA-based feature reduction  
- Model training & evaluation  
- API-based prediction endpoint  

## 2.3 Stakeholders
- Research Scientists  
- Materials Engineers  
- Developers & Data Scientists  
- Students / Academic Researchers  

---

# 3. System Requirements

## 3.1 Functional Requirements
- Load and parse spectral CSV data  
- Apply preprocessing (baseline removal, smoothing, normalization)  
- Extract engineered features  
- Train ML models for prediction  
- Save trained models  
- Deploy prediction API  
- Accept uploaded spectral files and return predictions  

## 3.2 Non-Functional Requirements
### Performance:
- API response time < 500 ms for a single prediction
- Training pipeline should process 1000 spectra < 2 minutes

### Reliability:
- 95% uptime (if deployed on cloud)
- Model loading must not exceed 2 seconds

### Usability:
- API accessible from Postman, cURL, or UI

### Security:
- Accept only `.csv` format
- Sanitize user inputs

### Maintainability:
- Modular architecture
- Separate preprocessing, feature extraction, training, and API layers

---

# 4. System Constraints
- Input files must contain *wavelength* and *absorbance* columns  
- Dataset should be formatted consistently  
- Models rely on numeric data only  

---

# 5. Dataset Requirements

## 5.1 Spectral Input Format

| wavelength | absorbance |
|------------|------------|
| 400        | 0.12       |
| 401        | 0.13       |

Range: 200–4000 cm⁻¹ (IR) or according to sensor type.  

## 5.2 Metadata Format

| file        | corrosion_rate | grade  |
|-------------|----------------|--------|
| sample1.csv | 0.52           | High   |

---

# 6. Assumptions and Dependencies
- Spectra are pre-aligned (same wavelength spacing)
- Models depend on RandomForest (sklearn)
- API depends on FastAPI, Uvicorn

---

# 7. Acceptance Criteria
- Regression RMSE < 0.2 (target goal)
- Classification accuracy > 85%
- API prediction endpoint functional and tested

---

# 8. Appendices
- Project code: preprocessing → feature extraction → training → API
- Future work: dashboard integration, deep learning models

---
