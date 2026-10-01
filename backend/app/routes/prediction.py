import sys
from pathlib import Path
from fastapi import APIRouter, HTTPException

# Ensure project root is in sys.path
ROOT_DIR = Path(__file__).resolve().parents[3]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.predict import predict_price

try:
    from backend.app.schemas.laptop import LaptopInput
except ModuleNotFoundError:
    from app.schemas.laptop import LaptopInput


router = APIRouter(
    tags=["Prediction"]
)


@router.post("/predict")
def predict(laptop: LaptopInput):
    try:
        data = laptop.model_dump()
        price = predict_price(data)

        return {
            "success": True,
            "predicted_price": round(price, 2),
            "currency": "EUR"
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction error: {str(e)}"
        )