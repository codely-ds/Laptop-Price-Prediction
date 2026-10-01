import sys
from pathlib import Path
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

# Reports/Figures directory
FIGURES_DIR = BASE_DIR / "reports" / "figures"
FIGURES_DIR.mkdir(parents=True, exist_ok=True)


def price_distribution(df, show=False):
    plt.figure(figsize=(10, 6))
    sns.histplot(
        df["Price_euros"],
        kde=True,
        color="#3b82f6"
    )
    plt.title("Laptop Price Distribution (€)")
    plt.xlabel("Price (€)")
    plt.ylabel("Number of Laptops")
    plt.tight_layout()
    output_path = FIGURES_DIR / "price_distribution.png"
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    if show:
        plt.show()
    plt.close()
    print(f"Saved: {output_path}")


def company_price(df, show=False):
    plt.figure(figsize=(12, 6))
    sns.barplot(
        data=df,
        x="Company",
        y="Price_euros",
        estimator="mean",
        palette="viridis"
    )
    plt.xticks(rotation=45)
    plt.title("Average Laptop Price by Company (€)")
    plt.xlabel("Company")
    plt.ylabel("Average Price (€)")
    plt.tight_layout()
    output_path = FIGURES_DIR / "company_price.png"
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    if show:
        plt.show()
    plt.close()
    print(f"Saved: {output_path}")


def ram_price(df, show=False):
    plt.figure(figsize=(8, 6))
    sns.boxplot(
        data=df,
        x="Ram",
        y="Price_euros",
        palette="coolwarm"
    )
    plt.title("RAM vs Laptop Price (€)")
    plt.xlabel("RAM (GB)")
    plt.ylabel("Price (€)")
    plt.tight_layout()
    output_path = FIGURES_DIR / "ram_price.png"
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    if show:
        plt.show()
    plt.close()
    print(f"Saved: {output_path}")


def type_price(df, show=False):
    plt.figure(figsize=(12, 6))
    sns.boxplot(
        data=df,
        x="TypeName",
        y="Price_euros",
        palette="magma"
    )
    plt.xticks(rotation=45)
    plt.title("Laptop Category vs Price (€)")
    plt.xlabel("Category")
    plt.ylabel("Price (€)")
    plt.tight_layout()
    output_path = FIGURES_DIR / "type_price.png"
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    if show:
        plt.show()
    plt.close()
    print(f"Saved: {output_path}")


def generate_all_visualizations(data_path=None, show=False):
    if data_path is None:
        data_path = BASE_DIR / "data" / "processed" / "laptop_price_cleaned.csv"
        if not data_path.exists():
            data_path = BASE_DIR / "data" / "raw" / "laptop_price.csv"

    print(f"Loading data for visualizations from: {data_path}")
    df = pd.read_csv(data_path, encoding="latin1")

    # Clean Ram if needed for plotting
    if df["Ram"].dtype == object:
        df["Ram"] = df["Ram"].astype(str).str.replace("GB", "", regex=False).astype(float)

    price_distribution(df, show=show)
    company_price(df, show=show)
    ram_price(df, show=show)
    type_price(df, show=show)
    print("All visualizations generated successfully.")


if __name__ == "__main__":
    generate_all_visualizations(show=False)