# 🧩 Functional Requirements Specification (FRS)
## Project: Data-Driven Material Performance Analysis using Spectroscopic Data & ML  
### Version 1.0  
### Prepared by: Sourav Kumar Hazra

---

# 1. Introduction
This FRS document provides a **detailed breakdown of functional requirements** of the system, describing its behavior and expected outputs.

---

# 2. Core Functional Modules

## 2.1 Module A — Data Preprocessing
### Description
Cleans raw spectral data for further processing.

### Functional Requirements
| ID | Requirement | Priority |
|----|-------------|----------|
| A1 | Load CSV spectral file | High |
| A2 | Validate columns: wavelength, absorbance | High |
| A3 | Apply baseline correction | High |
| A4 | Apply Savitzky–Golay smoothing | High |
| A5 | Apply min–max normalization | High |
| A6 | Return processed spectrum | High |

---

## 2.2 Module B — Feature Extraction
### Functional Requirements
| ID | Requirement | Priority |
|----|-------------|----------|
| B1 | Detect peaks using find_peaks() | High |
| B2 | Extract count, mean height, max height | High |
| B3 | Compute mean, std, max, min of signal | High |
| B4 | Optional PCA feature reduction | Medium |
| B5 | Return final feature vector | High |

---

## 2.3 Module C — Machine Learning Models
### Regression Model
| ID | Requirement | Priority |
|----|-------------|----------|
| C1 | Train RandomForestRegressor | High |
| C2 | Predict corrosion resistance | High |
| C3 | Store model with joblib | High |

### Classification Model
| ID | Requirement | Priority |
|----|-------------|----------|
| C4 | Train RandomForestClassifier | High |
| C5 | Predict material grade | High |

---

## 2.4 Module D — Prediction API
### Functional Requirements
| ID | Requirement | Priority |
|----|-------------|----------|
| D1 | Accept `.csv` upload | High |
| D2 | Process spectral data | High |
| D3 | Extract ML features | High |
| D4 | Generate regression prediction | High |
| D5 | Generate classification prediction | High |
| D6 | Return JSON response | High |

---

## 2.5 Module E — Visualization (Optional)
| ID | Requirement | Priority |
|----|-------------|----------|
| E1 | Plot raw & processed spectra | Medium |
| E2 | Plot detected peaks | Medium |

---

# 3. External Interface Requirements

## 3.1 API Interface
