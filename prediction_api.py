from fastapi import FastAPI, UploadFile
import pandas as pd
import joblib
import numpy as np

from data_preprocessing import SpectralPreprocessor
from feature_extraction import FeatureExtractor

app = FastAPI()

reg_model = joblib.load("corrosion_reg_model.pkl")
cls_model = joblib.load("material_grade_model.pkl")

pre = SpectralPreprocessor()
fe = FeatureExtractor()

@app.post("/predict/")
async def predict(file: UploadFile):

    df = pd.read_csv(file.file)
    x, y = pre.preprocess(df)
    features = fe.extract(x, y).reshape(1, -1)

    corrosion_rate = reg_model.predict(features)[0]
    material_grade = cls_model.predict(features)[0]

    return {
        "predicted_corrosion_rate_mm_per_year": float(corrosion_rate),
        "predicted_material_grade": material_grade
    }
