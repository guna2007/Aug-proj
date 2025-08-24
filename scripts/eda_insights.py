import pandas as pd

def eda_summary(df):
    insights = {}
    print("\nReading product category translation file...")
    tr_df = pd.read_csv("../data/processed/translation_clean.csv")

    print("\nAnalyzing dataset shape...")
    insights["shape"] = df.shape

    print("\nCalculating delivery performance...")
    if "delivered_late" in df.columns:
        late_rate = df["delivered_late"].value_counts().get(1, 0) / len(df["delivered_late"]) * 100
        insights["late_rate"] = f"{late_rate:.2f}% of orders delivered late"

    print("\nSummarizing review score distribution...")
    if "review_score" in df.columns:
        review_counts = df["review_score"].value_counts(normalize=True).sort_index()
        insights["review_distribution"] = review_counts.round(3).to_dict()

    print("\nIdentifying top product categories...")
    if "product_category_name" in df.columns:
        top_categories = df["product_category_name"].value_counts().head(5).to_dict()
        translation_dict = dict(zip(
            tr_df["product_category_name"],
            tr_df["product_category_name_english"]
        ))

        translated_top_dict = {
            translation_dict[k]: v for k, v in top_categories.items() if k in translation_dict
        }

        insights["top_categories"] = translated_top_dict

    print("\nComputing correlations with delivery delay...")
    numeric_cols = df.select_dtypes(include="number")
    if "delivered_late" in numeric_cols.columns:
        corr = numeric_cols.corr()["delivered_late"].sort_values(ascending=False)
        insights["delay_correlations"] = corr.round(3).head(10).to_dict()

    print("\nCalculating average delivery time...")
    if "delivery_time_days" in df.columns:
        avg_time = df["delivery_time_days"].mean()
        insights["avg_delivery_time_days"] = round(avg_time, 2)

    return insights

print("\nLoading final ML-ready dataset...")
final_df = pd.read_csv("../data/processed/final_ml_ready.csv")

print("\nGenerating EDA insights from dataset...")
insights = eda_summary(final_df)

print("\nEDA Insights Generated Successfully:")
for key, value in insights.items():
    print(f"\n**{key}:")
    print(value)
