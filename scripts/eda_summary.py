import pandas as pd

def print_summary():
    # Load dataset
    print("\nLoading cleaned dataset...")
    df = pd.read_csv("../data/processed/final_ml_ready.csv")

    print("\n==== EDA SUMMARY ====\n")

    # Shape
    print("---- Dataset Shape ----")
    print(f"{df.shape[0]} rows, {df.shape[1]} columns\n")

    # Column Info
    print("---- Column Data Types ----")
    print(df.dtypes)
    print()

    # Missing Values
    print("---- Missing Values ----")
    missing = df.isnull().sum()
    print(missing[missing > 0])
    print()

    # Duplicates
    print("---- Duplicates ----")
    print(f"Total Duplicated Rows: {df.duplicated().sum()}\n")

    # Numeric Summary
    print("---- Numeric Summary ----")
    print(df.describe().transpose())
    print()

    # Categorical Summary (top categories)
    print("---- Categorical Features (Top 5 Values Each) ----")
    cat_cols = df.select_dtypes(include=["object"]).columns
    for col in cat_cols:
        print(f"\nColumn: {col}")
        print(df[col].value_counts().head(5))
        print()

print_summary()
