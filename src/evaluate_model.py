import pandas as pd
import joblib
import matplotlib.pyplot as plt

from pathlib import Path

from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = (
    BASE_DIR /
    "data" /
    "processed" /
    "laptop_price_cleaned.csv"
)

MODEL_PATH = (
    BASE_DIR /
    "models" /
    "best_model.pkl"
)


def evaluate():

    df = pd.read_csv(DATA_PATH)

    X = df.drop(columns=["Price_euros"])
    y = df["Price_euros"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    model = joblib.load(MODEL_PATH)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    rmse = mean_squared_error(
        y_test,
        predictions
    ) ** 0.5

    r2 = r2_score(
        y_test,
        predictions
    )

    print("Model Evaluation")
    print("----------------")
    print("MAE :", round(mae, 2))
    print("RMSE:", round(rmse, 2))
    print("R²  :", round(r2, 4))

    plt.figure(figsize=(8, 6))

    plt.scatter(
        y_test,
        predictions,
        alpha=0.6
    )

    plt.xlabel("Actual Price")
    plt.ylabel("Predicted Price")

    plt.title(
        "Actual vs Predicted Laptop Price"
    )

    plt.tight_layout()

    plt.savefig(
        BASE_DIR /
        "reports" /
        "figures" /
        "actual_vs_predicted.png"
    )

    plt.show()


if __name__ == "__main__":
    evaluate()