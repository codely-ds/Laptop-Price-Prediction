from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "raw" / "laptop_price.csv"

def load_data():
    """
    Load laptop price dataset
    """

    df = pd.read_csv(DATA_PATH, encoding='latin')
    return df

if __name__ == "__main__":
    df = load_data()

    print("Dataset loaded successfully")
    print("shape:", df.shape)
    print("\ncolumns:")
    print(df.columns.tolist())