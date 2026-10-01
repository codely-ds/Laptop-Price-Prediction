import sys
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Ensure project root is in sys.path
ROOT_DIR = Path(__file__).resolve().parents[2]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

try:
    from backend.app.routes.prediction import router
except ModuleNotFoundError:
    from app.routes.prediction import router

app = FastAPI(
    title="Laptop Price Prediction API",
    description="Machine learning API for predicting laptop prices based on hardware specifications",
    version="1.0.0"
)

# Enable CORS for frontend clients
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    router,
    prefix="/api"
)


@app.get("/")
def root():
    return {
        "message": "Laptop Price Prediction API",
        "docs_url": "/docs",
        "health_check": "/health",
        "prediction_endpoint": "/api/predict"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "laptop-price-predictor"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.app.main:app", host="0.0.0.0", port=8000, reload=True)