import sys
from pathlib import Path
import joblib
import pandas as pd

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from src.data_cleaning import clean_data
from src.feature_engineering import feature_engineering

# Model path
MODEL_PATH = BASE_DIR / "models" / "best_model.pkl"

# Global model cache
_model = None


def get_model():
    global _model
    if _model is None:
        if not MODEL_PATH.exists():
            raise FileNotFoundError(
                f"Trained model not found at {MODEL_PATH}. Run src/train_model.py first."
            )
        _model = joblib.load(MODEL_PATH)
    return _model


def predict_price(laptop_data: dict) -> float:
    """
    Predict laptop price given a dictionary of laptop specifications.
    """
    # 1. Convert input to DataFrame
    df = pd.DataFrame([laptop_data])

    # 2. Data Cleaning
    df = clean_data(df)

    # 3. Feature Engineering
    df = feature_engineering(df)

    # 4. Prediction
    model = get_model()
    prediction = model.predict(df)

    return float(prediction[0])


if __name__ == "__main__":
    sample_laptop = {
        "Company": "Dell",
        "Product": "Inspiron 3567",
        "TypeName": "Notebook",
        "Inches": 15.6,
        "ScreenResolution": "Full HD 1920x1080",
        "Cpu": "Intel Core i5 7200U 2.5GHz",
        "Ram": "8GB",
        "Memory": "256GB SSD",
        "Gpu": "Intel HD Graphics 620",
        "OpSys": "Windows 10",
        "Weight": "1.86kg"
    }
    price = predict_price(sample_laptop)
    print(f"Sample Laptop Predicted Price: €{price:.2f}")