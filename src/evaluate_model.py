import sys
from pathlib import Path
import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

DATA_PATH = BASE_DIR / "data" / "processed" / "laptop_price_cleaned.csv"
MODEL_PATH = BASE_DIR / "models" / "best_model.pkl"
FIGURES_DIR = BASE_DIR / "reports" / "figures"
FIGURES_DIR.mkdir(parents=True, exist_ok=True)


def evaluate(show=False):
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Processed dataset not found at {DATA_PATH}")
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Trained model not found at {MODEL_PATH}")

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

    mae = mean_absolute_error(y_test, predictions)
    rmse = mean_squared_error(y_test, predictions) ** 0.5
    r2 = r2_score(y_test, predictions)

    print("\n==========================================")
    print("           MODEL EVALUATION REPORT         ")
    print("==========================================")
    print(f"Mean Absolute Error (MAE) : €{mae:.2f}")
    print(f"Root Mean Squared Err (RMSE): €{rmse:.2f}")
    print(f"R² Score (Coefficient)    : {r2:.4f}")
    print("==========================================\n")

    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, predictions, alpha=0.6, color="#3b82f6", edgecolors="none")
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--", lw=2)
    plt.xlabel("Actual Price (€)")
    plt.ylabel("Predicted Price (€)")
    plt.title("Actual vs Predicted Laptop Price (€)")
    plt.tight_layout()

    output_fig = FIGURES_DIR / "actual_vs_predicted.png"
    plt.savefig(output_fig, dpi=300, bbox_inches="tight")
    if show:
        plt.show()
    plt.close()
    print(f"Saved evaluation plot to: {output_fig}")

    return {"mae": mae, "rmse": rmse, "r2": r2}


if __name__ == "__main__":
    evaluate(show=False)