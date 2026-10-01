import sys
from pathlib import Path
import pytest
import pandas as pd

# Add project root to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.feature_engineering import feature_engineering
from src.predict import predict_price
from backend.app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_data_loader():
    df = load_data()
    assert not df.empty
    assert "Price_euros" in df.columns

def test_data_cleaning_and_feature_engineering():
    df = load_data()
    cleaned = clean_data(df)
    assert "laptop_ID" not in cleaned.columns
    assert cleaned["Ram"].dtype == float or str(cleaned["Ram"].dtype).startswith("float")

    engineered = feature_engineering(cleaned)
    expected_cols = ["CPU_Brand", "CPU_Speed", "Screen_Width", "Screen_Height", "Touchscreen", "IPS", "SSD_GB", "HDD_GB", "Flash_GB", "Hybrid_GB"]
    for col in expected_cols:
        assert col in engineered.columns

def test_predict_price_various_configs():
    laptops = [
        {
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
        },
        {
            "Company": "Apple",
            "Product": "MacBook Pro",
            "TypeName": "Ultrabook",
            "Inches": 13.3,
            "ScreenResolution": "IPS Panel Retina Display 2560x1600",
            "Cpu": "Intel Core i5 2.3GHz",
            "Ram": "8GB",
            "Memory": "128GB SSD",
            "Gpu": "Intel Iris Plus Graphics 640",
            "OpSys": "macOS",
            "Weight": "1.37kg"
        },
        {
            "Company": "Asus",
            "Product": "ROG GL553VE",
            "TypeName": "Gaming",
            "Inches": 15.6,
            "ScreenResolution": "Full HD 1920x1080",
            "Cpu": "Intel Core i7 7700HQ 2.8GHz",
            "Ram": "16GB",
            "Memory": "128GB SSD + 1TB HDD",
            "Gpu": "Nvidia GeForce GTX 1050 Ti",
            "OpSys": "Windows 10",
            "Weight": "2.5kg"
        },
        {
            "Company": "HP",
            "Product": "Stream 14",
            "TypeName": "Notebook",
            "Inches": 14.0,
            "ScreenResolution": "1366x768",
            "Cpu": "Intel Celeron N3060 1.6GHz",
            "Ram": "4GB",
            "Memory": "32GB Flash Storage",
            "Gpu": "Intel HD Graphics 400",
            "OpSys": "Windows 10",
            "Weight": "1.44kg"
        }
    ]

    for laptop in laptops:
        price = predict_price(laptop)
        assert isinstance(price, float)
        assert price > 100.0

def test_api_endpoints():
    # Health check
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json().get("status") == "healthy"

    # Root endpoint
    res = client.get("/")
    assert res.status_code == 200
    assert "Laptop Price Prediction API" in res.json().get("message", "")

    # Prediction API
    payload = {
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
    res = client.post("/api/predict", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["success"] is True
    assert "predicted_price" in data
    assert data["currency"] == "EUR"
