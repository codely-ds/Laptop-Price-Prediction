import pytest
from src.predict import predict_price

def test_predict_price():
    sample_data = {
        "Company": "Dell",
        "Product": "Inspiron",
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
    price = predict_price(sample_data)
    print(f"Predicted price: {price}")
    assert isinstance(price, float)
    assert price > 0
