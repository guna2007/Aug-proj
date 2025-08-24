import pandas as pd

print("\nLoading model-ready dataset...")
df = pd.read_csv("../data/processed/olist_model_ready.csv")
print("Dataset loaded successfully.\n")

print("Selecting relevant business columns...")
business_cols = [
    "order_id", "customer_id", "customer_unique_id",
    "order_purchase_timestamp", "order_approved_at",
    "order_delivered_carrier_date", "order_delivered_customer_date",
    "order_estimated_delivery_date", "shipping_limit_date_x",
    "customer_city", "customer_state",
    "seller_id", "seller_city", "seller_state",
    "customer_seller_distance_km", "log_distance_seller_customer",
    "product_id", "product_category_name",
    "price", "freight_value", "num_items", "total_price",
    "payment_value", "payment_installments",
    "review_score", "has_review",
    "delivery_time_days", "approval_delay_days",
    "promised_delivery_days", "shipping_window_days",
    "is_delivered", "is_late", "delivered_late"
]
df = df[[col for col in business_cols if col in df.columns]]
print("Column selection completed.\n")

print("Converting date columns to datetime format...")
date_cols = [
    "order_purchase_timestamp", "order_approved_at",
    "order_delivered_carrier_date", "order_delivered_customer_date",
    "order_estimated_delivery_date", "shipping_limit_date_x"
]
for col in date_cols:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")
print("Datetime conversion completed.\n")

print("Extracting date components for trend analysis...")
df["purchase_year"] = df["order_purchase_timestamp"].dt.year
df["purchase_month"] = df["order_purchase_timestamp"].dt.month
df["purchase_day"] = df["order_purchase_timestamp"].dt.day
df["purchase_dayofweek"] = df["order_purchase_timestamp"].dt.day_name()
print("Date component extraction completed.\n")

print("Calculating delivery delay in days...")
if "order_delivered_customer_date" in df.columns and "order_estimated_delivery_date" in df.columns:
    df["delivery_delay_days"] = (
        (df["order_delivered_customer_date"] - df["order_estimated_delivery_date"])
        .dt.days
    )
    df["delivery_delay_days"] = df["delivery_delay_days"].fillna(0)
    df["delivery_delay_days"] = df["delivery_delay_days"].clip(lower=0)
print("Delivery delay calculation completed.\n")

print("Flagging successful deliveries...")
df["delivery_success"] = df["delivery_delay_days"].apply(lambda x: 1 if x <= 0 else 0)
print("Delivery success flag added.\n")

print("Calculating revenue and total cost...")
df["revenue"] = df["price"] * df["num_items"]
df["total_cost"] = df["revenue"] + df["freight_value"]
print("Revenue and cost calculations completed.\n")

print("Estimating profit margin proxy...")
df["profit_margin_proxy"] = df["price"] * 0.2  # assume 20% margin
print("Profit margin proxy added.\n")

output_path = "../data/processed/eda_business_ready.csv"
df.to_csv(output_path, index=False)

print("Business EDA dataset saved.")
print(f"\nFile location: {output_path}")
print(f"Final shape: {df.shape}\n")
print("Included columns:")
print(df.columns.tolist())
