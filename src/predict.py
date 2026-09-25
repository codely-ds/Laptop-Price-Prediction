# import joblib
# import pandas as pd

# from pathlib import Path


# BASE_DIR = Path(__file__).resolve().parent.parent

# MODEL_PATH = (
#     BASE_DIR /
#     "models" /
#     "best_model.pkl"
# )


# model = joblib.load(MODEL_PATH)


# def predict_price(laptop_data):

#     df = pd.DataFrame([laptop_data])

#     prediction = model.predict(df)

#     return float(prediction[0])



# =================================================================
# =================================================================

import joblib
import pandas as pd

from pathlib import Path

from src.data_cleaning import clean_data
from src.feature_engineering import feature_engineering


# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Model path
MODEL_PATH = BASE_DIR / "models" / "best_model.pkl"


# Load trained model
model = joblib.load(MODEL_PATH)


def predict_price(laptop_data):

    # -------------------------
    # 1. Convert input to DataFrame
    # -------------------------

    df = pd.DataFrame([laptop_data])


    # -------------------------
    # 2. Data Cleaning
    # -------------------------

    df = clean_data(df)


    # -------------------------
    # 3. Feature Engineering
    # -------------------------

    df = feature_engineering(df)


    # -------------------------
    # 4. Prediction
    # -------------------------

    prediction = model.predict(df)


    return float(prediction[0])