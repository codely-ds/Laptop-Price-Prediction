# from fastapi import APIRouter

# import sys
# from pathlib import Path

# sys.path.append(
#     str(
#         Path(__file__)
#         .resolve()
#         .parents[3]
#     )
# )

# from src.predict import predict_price

# from backend.app.schemas.laptop import LaptopInput


# router = APIRouter()


# @router.post("/predict")
# def predict(laptop: LaptopInput):

#     data = laptop.model_dump()

#     price = predict_price(data)

#     return {
#         "predicted_price": round(price, 2),
#         "currency": "EUR"
#     }


# =====================================================================
# =====================================================================

from fastapi import APIRouter, HTTPException

from src.predict import predict_price
from backend.app.schemas.laptop import LaptopInput


router = APIRouter(
    tags=["Prediction"]
)


@router.post("/predict")
def predict(laptop: LaptopInput):

    try:

        # Convert Pydantic model to dictionary
        data = laptop.model_dump()


        # Predict laptop price
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