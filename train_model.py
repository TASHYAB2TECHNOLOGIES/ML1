import os
import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_squared_error, accuracy_score

from data_preprocessing import SpectralPreprocessor
from feature_extraction import FeatureExtractor

pre = SpectralPreprocessor()
fe = FeatureExtractor()

df = pd.read_csv("spectral_dataset.csv")

feature_list = []
target_reg = []
target_cls = []

for file in df['file']:
    spec = pd.read_csv(f"spectra/{file}")
    x, y = pre.preprocess(spec)
    features = fe.extract(x, y)

    feature_list.append(features)
    target_reg.append(df[df['file'] == file]['corrosion_rate'].values[0])
    target_cls.append(df[df['file'] == file]['grade'].values[0])

X = np.array(feature_list)
y_reg = np.array(target_reg)
y_cls = np.array(target_cls)

X_train, X_test, y_train_reg, y_test_reg = train_test_split(
    X, y_reg, test_size=0.2, random_state=42
)

_, _, y_train_cls, y_test_cls = train_test_split(
    X, y_cls, test_size=0.2, random_state=42
)

reg_model = RandomForestRegressor(n_estimators=200)
reg_model.fit(X_train, y_train_reg)
reg_pred = reg_model.predict(X_test)
print("Regression RMSE:", np.sqrt(mean_squared_error(y_test_reg, reg_pred)))
joblib.dump(reg_model, "corrosion_reg_model.pkl")

cls_model = RandomForestClassifier(n_estimators=200)
cls_model.fit(X_train, y_train_cls)
cls_pred = cls_model.predict(X_test)
print("Classification Accuracy:", accuracy_score(y_test_cls, cls_pred))
joblib.dump(cls_model, "material_grade_model.pkl")
