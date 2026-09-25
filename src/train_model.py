# The target is price Error

# ===============================================

import pandas as pd
import joblib

from pathlib import Path

from sklearn.model_selection import (
    train_test_split,
    cross_val_score,
    KFold
)

from sklearn.compose import ColumnTransformer

from sklearn.pipeline import Pipeline

from sklearn.preprocessing import (
    OneHotEncoder,
    StandardScaler
)

from sklearn.impute import SimpleImputer

from sklearn.linear_model import (
    LinearRegression,
    Ridge,
    Lasso
)

from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor
)

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

PREPROCESSOR_PATH = (
    BASE_DIR /
    "models" /
    "preprocessor.pkl"
)


def prepare_data():

    df = pd.read_csv(DATA_PATH)

    X = df.drop(columns=["Price_euros"])

    y = df["Price_euros"]

    return X, y


def create_preprocessor(X):

    categorical_columns = X.select_dtypes(
        include=["object"]
    ).columns.tolist()

    numerical_columns = X.select_dtypes(
        exclude=["object"]
    ).columns.tolist()

    numerical_pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="median")
            ),
            (
                "scaler",
                StandardScaler()
            )
        ]
    )

    categorical_pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="most_frequent")
            ),
            (
                "encoder",
                OneHotEncoder(
                    handle_unknown="ignore"
                )
            )
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "num",
                numerical_pipeline,
                numerical_columns
            ),
            (
                "cat",
                categorical_pipeline,
                categorical_columns
            )
        ]
    )

    return preprocessor


# Train Multiple Models
def train_models(X_train, X_test, y_train, y_test):

    preprocessor = create_preprocessor(X_train)

    models = {

        "Linear Regression":
            LinearRegression(),

        "Ridge":
            Ridge(alpha=1.0),

        "Lasso":
            Lasso(alpha=0.1),

        "Random Forest":
            RandomForestRegressor(
                n_estimators=300,
                random_state=42,
                n_jobs=-1
            ),

        "Gradient Boosting":
            GradientBoostingRegressor(
                n_estimators=200,
                learning_rate=0.05,
                max_depth=3,
                random_state=42
            )
    }

    results = {}

    best_model = None
    best_r2 = float("-inf")

    for name, model in models.items():

        pipeline = Pipeline(
            steps=[
                (
                    "preprocessor",
                    preprocessor
                ),
                (
                    "model",
                    model
                )
            ]
        )

        pipeline.fit(
            X_train,
            y_train
        )

        predictions = pipeline.predict(
            X_test
        )

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

        results[name] = {
            "MAE": mae,
            "RMSE": rmse,
            "R2": r2
        }

        print(f"\n{name}")

        print("MAE :", round(mae, 2))
        print("RMSE:", round(rmse, 2))
        print("R2  :", round(r2, 4))

        if r2 > best_r2:

            best_r2 = r2
            best_model = pipeline

    return best_model, results

# Cross Validation
def cross_validate_model(model, X, y):

    kfold = KFold(
        n_splits=5,
        shuffle=True,
        random_state=42
    )

    scores = cross_val_score(
        model,
        X,
        y,
        cv=kfold,
        scoring="r2"
    )

    print("\nCross Validation R² Scores:")

    print(scores)

    print(
        "Mean CV R²:",
        round(scores.mean(), 4)
    )

    return scores


# Save Best Model 
def save_model(model):

    MODEL_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    joblib.dump(
        model,
        MODEL_PATH
    )

    print(
        f"\nModel saved to: {MODEL_PATH}"
    )

# Main Training Function
if __name__ == "__main__":

    X, y = prepare_data()

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    print("Training data:", X_train.shape)
    print("Testing data :", X_test.shape)

    best_model, results = train_models(
        X_train,
        X_test,
        y_train,
        y_test
    )

    cross_validate_model(
        best_model,
        X_train,
        y_train
    )

    save_model(best_model)

    print("\nModel training completed.")