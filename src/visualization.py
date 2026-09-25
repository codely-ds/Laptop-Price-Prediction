from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Reports/Figures directory
FIGURES_DIR = BASE_DIR / "reports" / "figures"

# Create directory if it doesn't exist
FIGURES_DIR.mkdir(parents=True, exist_ok=True)


def price_distribution(df):

    plt.figure(figsize=(10, 6))

    sns.histplot(
        df["Price_euros"],
        kde=True
    )

    plt.title("Laptop Price Distribution")
    plt.xlabel("Price (€)")
    plt.ylabel("Number of Laptops")

    plt.tight_layout()

    plt.savefig(
        FIGURES_DIR / "price_distribution.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

    plt.close()


def company_price(df):

    plt.figure(figsize=(12, 6))

    sns.barplot(
        data=df,
        x="Company",
        y="Price_euros",
        estimator="mean"
    )

    plt.xticks(rotation=45)

    plt.title("Average Laptop Price by Company")

    plt.tight_layout()

    plt.savefig(
        FIGURES_DIR / "company_price.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

    plt.close()


def ram_price(df):

    plt.figure(figsize=(8, 6))

    sns.boxplot(
        data=df,
        x="Ram",
        y="Price_euros"
    )

    plt.title("RAM vs Laptop Price")

    plt.tight_layout()

    plt.savefig(
        FIGURES_DIR / "ram_price.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

    plt.close()


def type_price(df):

    plt.figure(figsize=(12, 6))

    sns.boxplot(
        data=df,
        x="TypeName",
        y="Price_euros"
    )

    plt.xticks(rotation=45)

    plt.title("Laptop Type vs Price")

    plt.tight_layout()

    plt.savefig(
        FIGURES_DIR / "type_price.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

    plt.close()