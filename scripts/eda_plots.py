import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Paths
DATA_PATH = os.path.join("..", "data", "processed", "final_ml_ready.csv")
FIG_PATH = os.path.join("..", "reports", "basic_plots")

os.makedirs(FIG_PATH, exist_ok=True)

def plot_late_rate(df):
    print("\nPlotting delivery performance (On-Time vs Late)...")
    late_rate = df["delivered_late"].mean() * 100
    values = [100 - late_rate, late_rate]
    labels = ["On-Time", "Late"]

    plt.figure(figsize=(6, 4))
    sns.barplot(x=labels, y=values, hue=labels, palette=["#4CAF50", "#F44336"])
    plt.ylabel("Percentage (%)")
    plt.title("Delivery Performance (On-Time vs Late)")
    for i, val in enumerate(values):
        plt.text(i, val + 1, f"{val:.1f}%", ha='center')
    plt.savefig(os.path.join(FIG_PATH, "late_rate.png"))
    plt.close()
    print("Saved: late_rate.png")

def plot_review_distribution(df):
    print("\nPlotting review score distribution...")
    review_counts = df["review_score"].value_counts(normalize=True).sort_index()

    plt.figure(figsize=(6, 4))
    sns.barplot(
        x=review_counts.index.to_list(),
        y=review_counts.values.tolist(),
        hue=review_counts.index.to_list(),
        palette="Blues",
        legend=False
    )
    for i, v in enumerate(review_counts.values):
        plt.text(i, v + 0.005, f"{v:.2f}", ha="center", fontsize=10)

    plt.ylabel("Proportion")
    plt.xlabel("Review Score")
    plt.title("Review Score Distribution")
    plt.savefig(os.path.join(FIG_PATH, "review_distribution.png"))
    plt.close()
    print("Saved: review_distribution.png")

def plot_top_categories(df, n=10):
    print("\nPlotting top product categories...")
    top_categories = df["product_category_name"].value_counts().head(5).to_dict()
    translation_path = "../data/processed/translation_clean.csv"

    if not os.path.exists(translation_path):
        print(f"Translation file not found at: {translation_path}")
        return

    tr_df = pd.read_csv(translation_path)
    translation_dict = dict(zip(
        tr_df["product_category_name"],
        tr_df["product_category_name_english"]
    ))

    translated_top_dict = {
        translation_dict[k]: v for k, v in top_categories.items() if k in translation_dict
    }

    plt.figure(figsize=(8, 6))
    sns.barplot(
        y=list(translated_top_dict.keys()),
        x=list(translated_top_dict.values()),
        hue=list(translated_top_dict.keys()),
        palette="viridis",
        legend=False
    )
    for i, v in enumerate(translated_top_dict.values()):
        plt.text(v + 1, i, str(v), va="center", fontsize=10)

    plt.xlabel("Order Count")
    plt.ylabel("Category")
    plt.title("Top 5 Product Categories")
    plt.savefig(os.path.join(FIG_PATH, "top_categories.png"))
    plt.close()
    print("Saved: top_categories.png")

def plot_delivery_time_distribution(df):
    print("\nPlotting delivery time distribution...")
    plt.figure(figsize=(8, 5))
    sns.histplot(df["delivery_time_days"].dropna(), bins=40, kde=False, color="skyblue")
    mean_val = df["delivery_time_days"].mean()
    plt.axvline(mean_val, color="red", linestyle="--", label="Mean")
    plt.text(mean_val, -plt.ylim()[1]*0.02, f"{mean_val:.1f}", color="red", ha="center", va="top", fontsize=10)
    plt.xlabel("Delivery Time (days)")
    plt.ylabel("Order Count")
    plt.title("Delivery Time Distribution")
    plt.legend()
    plt.savefig(os.path.join(FIG_PATH, "delivery_time_distribution.png"))
    plt.close()
    print("Saved: delivery_time_distribution.png")

def plot_delay_correlations(df):
    print("\nPlotting top features correlated with late delivery...")
    corr = df.corr(numeric_only=True)["delivered_late"].drop([
        "delivered_late",
        "geolocation_zip_code_prefix_x",
        "customer_zip_code_prefix",
        "is_late",
        "log_distance_seller_customer",
        "seller_zip_code_prefix",
        "geolocation_zip_code_prefix_y"
    ]).abs().sort_values(ascending=False).head(10)

    plt.figure(figsize=(8, 6))
    sns.barplot(
        x=corr.values,
        y=corr.index,
        hue=corr.index,
        palette="coolwarm",
        dodge=False,
        legend=False
    )
    for i, v in enumerate(corr.values):
        plt.text(v + 0.01, i, f"{v:.2f}", va="center", fontsize=10, color="black")

    plt.xlabel("Correlation with Late Delivery")
    plt.ylabel("Feature")
    plt.title("Top Correlated Features with Late Delivery")
    plt.savefig(os.path.join(FIG_PATH, "delay_correlations.png"))
    plt.close()
    print("Saved: delay_correlations.png")

print("\nStarting EDA Plot Generation...")
df = pd.read_csv(DATA_PATH)

plot_late_rate(df)
plot_review_distribution(df)
plot_top_categories(df)
plot_delivery_time_distribution(df)
plot_delay_correlations(df)

print(f"\nAll plots saved in: {FIG_PATH}")
