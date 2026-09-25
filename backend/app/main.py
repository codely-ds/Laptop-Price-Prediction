from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from app.routes.prediction import router
from backend.app.routes.prediction import router

app = FastAPI(
    title="Laptop Price Prediction API",
    description="API for predicting laptop prices",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
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
        "message": "Laptop Price Prediction API"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }