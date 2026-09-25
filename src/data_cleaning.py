import pandas as pd


def clean_data(df):

    df = df.copy()

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove unnecessary ID column
    if "laptop_ID" in df.columns:
        df = df.drop(columns=["laptop_ID"])

    # Clean RAM
    df["Ram"] = (
        df["Ram"]
        .str.replace("GB", "", regex=False)
        .astype(float)
    )

    # Clean Weight
    df["Weight"] = (
        df["Weight"]
        .str.replace("kg", "", regex=False)
        .astype(float)
    )

    return df


if __name__ == "__main__":

    df = pd.read_csv(
        "../data/raw/laptop_price.csv",
        encoding="latin1"
    )

    df = clean_data(df)

    print(df.head())
    print(df.dtypes)