import pandas as pd

# Load dataset
print("Loading model-ready dataset...")
df = pd.read_csv("../data/processed/olist_model_ready.csv")
print("Initial shape:", df.shape)

# Drop raw timestamp columns
print("Dropping raw timestamp columns if present...")
timestamp_cols = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
    "shipping_limit_date_x",
    "shipping_limit_date_y"
]
df.drop(columns=[col for col in timestamp_cols if col in df.columns], inplace=True)

# Drop raw lat/lng columns
print("Dropping raw latitude and longitude columns if present...")
latlng_cols = [
    "customer_lat", "customer_lng",
    "seller_lat", "seller_lng"
]
df.drop(columns=[col for col in latlng_cols if col in df.columns], inplace=True)

# Drop duplicate target column if both exist
if "delivered_late" in df.columns and "delayed" in df.columns:
    print("Dropping duplicate target column: 'delivered_late'")
    df.drop(columns=["delivered_late"], inplace=True)

# Drop redundant index column if present
if "Unnamed: 0" in df.columns:
    print("Dropping redundant index column: 'Unnamed: 0'")
    df.drop(columns=["Unnamed: 0"], inplace=True)

# Save cleaned dataset
print("Saving cleaned dataset to final_ml_ready.csv...")
df.to_csv("../data/processed/final_ml_ready.csv", index=False)
print("Cleanup complete. Saved ML-ready dataset at: ../data/processed/final_ml_ready.csv")
print("Shape:", df.shape)