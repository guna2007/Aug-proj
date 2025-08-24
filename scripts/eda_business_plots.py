import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Define input and output paths
INPUT_FILE = "../data/processed/eda_business_ready.csv"
OUTPUT_DIR = "../reports/business/"

print("Setting up output directory...")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Configure plot style
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

print("Loading datasets...")
df = pd.read_csv(INPUT_FILE)
translation = pd.read_csv("../data/processed/translation_clean.csv")
payments = pd.read_csv("../data/processed/order_payment_clean.csv")
print("Datasets loaded successfully.")

print("Merging product category translations...")
df = df.merge(translation, how="left", on="product_category_name")

print("Merging primary payment type per order...")
payments_primary = payments.sort_values("payment_sequential").drop_duplicates("order_id")
df = df.merge(payments_primary[["order_id", "payment_type"]], how="left", on="order_id")

print("Parsing purchase timestamps...")
if "order_purchase_timestamp" in df.columns:
    df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"], errors="coerce")

print("Validating required columns for plotting...")
required_cols = [
    "product_category_name_english", "delivered_late", "delivery_delay_days",
    "customer_state", "seller_state", "payment_type", "payment_value",
    "order_purchase_timestamp", "order_id", "customer_id"
]
missing = [c for c in required_cols if c not in df.columns]
if missing:
    raise ValueError(f"Missing required columns: {missing}")
print("All required columns are present.")

# =============== 1. Late Delivery Rate by Product Category ===============
print("Generating plot: Late Delivery Rate by Product Category...")
category_late = (
    df.groupby("product_category_name_english")["delivered_late"]
    .mean()
    .sort_values(ascending=False)
    .head(15)
)
plt.figure()
sns.barplot(x=category_late.values, y=category_late.index, hue=category_late.index, legend=False)
plt.title("Late Delivery Rate by Product Category (Top 15)")
plt.xlabel("Late Delivery Rate (%)")
plt.ylabel("Product Category")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "eda_late_by_category.png"))

# =============== 2. Avg Delivery Delay vs Customer State ===============
print("Generating plot: Average Delivery Delay by Customer State...")
state_delay = (
    df.groupby("customer_state")["delivery_delay_days"]
    .mean()
    .sort_values(ascending=False)
)
plt.figure()
sns.barplot(x=state_delay.values, y=state_delay.index, hue=state_delay.index, legend=False)
plt.title("Average Delivery Delay by Customer State")
plt.xlabel("Avg Delay (Days)")
plt.ylabel("Customer State")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "eda_delay_by_state.png"))

# =============== 3. Avg Delivery Delay vs Seller State ===============
print("Generating plot: Average Delivery Delay by Seller State...")
seller_delay = (
    df.groupby("seller_state")["delivery_delay_days"]
    .mean()
    .sort_values(ascending=False)
)
plt.figure()
sns.barplot(x=seller_delay.values, y=seller_delay.index, hue=seller_delay.index, legend=False)
plt.title("Average Delivery Delay by Seller State")
plt.xlabel("Avg Delay (Days)")
plt.ylabel("Seller State")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "eda_delay_by_seller.png"))

# =============== 4. Payment Type vs Late Deliveries ===============
print("Generating plot: Late Delivery Rate by Payment Type...")
payment_late = df.groupby("payment_type")["delivered_late"].mean().sort_values()
plt.figure()
sns.barplot(x=payment_late.index, y=payment_late.values, hue=payment_late.index, legend=False)
plt.title("Late Delivery Rate by Payment Type")
plt.ylabel("Late Delivery Rate")
plt.xlabel("Payment Type")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "eda_late_by_payment.png"))

# =============== 5. Order Value vs Delivery Performance ===============
print("Generating plot: Order Value vs Delivery Performance...")
plt.figure()
sns.boxplot(data=df, x="delivered_late", y="payment_value", showfliers=False)
plt.title("Order Value vs Delivery Performance")
plt.xlabel("Delivered Late (0 = On-time, 1 = Late)")
plt.ylabel("Order Value")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "eda_order_value_vs_delay.png"))

# =============== 6. Monthly Trend of Late Deliveries ===============
print("Generating plot: Monthly Trend of Late Deliveries...")
df["order_month"] = df["order_purchase_timestamp"].dt.to_period("M")
monthly_trend = df.groupby("order_month")["delivered_late"].mean()

plt.figure()
monthly_trend.plot(kind="line", marker="o", color="teal")
plt.title("Monthly Trend of Late Deliveries")
plt.ylabel("Late Delivery Rate")
plt.xlabel("Month")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "eda_monthly_trend.png"))

print("All business EDA plots generated and saved to:", OUTPUT_DIR)
