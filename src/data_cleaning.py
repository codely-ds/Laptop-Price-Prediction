from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]


def clean_data(df):
    df = df.copy()

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove unnecessary ID column
    if "laptop_ID" in df.columns:
        df = df.drop(columns=["laptop_ID"])

    # Clean RAM (support '8GB', '8', 8, 8.0)
    if "Ram" in df.columns:
        if df["Ram"].dtype == object or isinstance(df["Ram"].iloc[0], str):
            df["Ram"] = (
                df["Ram"]
                .astype(str)
                .str.replace("GB", "", case=False, regex=False)
                .str.strip()
                .astype(float)
            )
        else:
            df["Ram"] = df["Ram"].astype(float)

    # Clean Weight (support '1.86kg', '1.86', 1.86)
    if "Weight" in df.columns:
        if df["Weight"].dtype == object or isinstance(df["Weight"].iloc[0], str):
            df["Weight"] = (
                df["Weight"]
                .astype(str)
                .str.replace("kg", "", case=False, regex=False)
                .str.strip()
                .astype(float)
            )
        else:
            df["Weight"] = df["Weight"].astype(float)

    return df


if __name__ == "__main__":
    data_path = BASE_DIR / "data" / "raw" / "laptop_price.csv"
    if data_path.exists():
        df = pd.read_csv(data_path, encoding="latin1")
        df = clean_data(df)
        print(df.head())
        print(df.dtypes)
    else:
        print(f"Data file not found at {data_path}")