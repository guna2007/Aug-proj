import pandas as pd
import numpy as np
from math import radians, sin, cos, sqrt, atan2

print("\nLoading cleaned datasets...")
orders = pd.read_csv("../data/processed/order_clean.csv")
order_items = pd.read_csv("../data/processed/order_item_clean.csv")
customers = pd.read_csv("../data/processed/customer_clean.csv")
products = pd.read_csv("../data/processed/product_clean.csv")
sellers = pd.read_csv("../data/processed/seller_clean.csv")
payments = pd.read_csv("../data/processed/order_payment_clean.csv")
reviews = pd.read_csv("../data/processed/order_review_clean.csv")
geolocation = pd.read_csv("../data/processed/geolocation_clean.csv")

print("\nComputing average geolocation coordinates by zip code...")
geo_avg = geolocation.groupby("geolocation_zip_code_prefix").agg({
    "geolocation_lat": "mean",
    "geolocation_lng": "mean"
}).reset_index()

print("\nMerging shipping limit timestamps into orders...")
orders = orders.merge(
    order_items[["order_id", "shipping_limit_date"]],
    on="order_id",
    how="left"
)

print("\nMerging geolocation data into customers and sellers...")
customers = customers.merge(
    geo_avg,
    how="left",
    left_on="customer_zip_code_prefix",
    right_on="geolocation_zip_code_prefix"
).rename(columns={"geolocation_lat": "customer_lat", "geolocation_lng": "customer_lng"})

sellers = sellers.merge(
    geo_avg,
    how="left",
    left_on="seller_zip_code_prefix",
    right_on="geolocation_zip_code_prefix"
).rename(columns={"geolocation_lat": "seller_lat", "geolocation_lng": "seller_lng"})

print("\nCalculating customer-seller distances...")
orders_geo = orders.merge(customers[["customer_id", "customer_lat", "customer_lng"]], on="customer_id", how="left")
orders_geo = orders_geo.merge(order_items.merge(sellers[["seller_id", "seller_lat", "seller_lng"]], on="seller_id", how="left"),
                              on="order_id", how="left")

def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1)*cos(lat2)*sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return R * c

orders_geo["customer_seller_distance_km"] = orders_geo.apply(
    lambda row: haversine(row["customer_lat"], row["customer_lng"], row["seller_lat"], row["seller_lng"])
    if pd.notnull(row["customer_lat"]) and pd.notnull(row["seller_lat"]) else None,
    axis=1
)

orders = orders.merge(
    orders_geo[["order_id", "customer_seller_distance_km"]].groupby("order_id").mean().reset_index(),
    on="order_id",
    how="left"
)

print("Distance feature added.\n")

print("Generating delivery-related features...")
orders["order_purchase_timestamp"] = pd.to_datetime(orders["order_purchase_timestamp"])
orders["order_approved_at"] = pd.to_datetime(orders["order_approved_at"])
orders["order_delivered_customer_date"] = pd.to_datetime(orders["order_delivered_customer_date"])
orders["order_estimated_delivery_date"] = pd.to_datetime(orders["order_estimated_delivery_date"])
orders["shipping_limit_date"] = pd.to_datetime(orders["shipping_limit_date"])

orders["is_delivered"] = orders["order_delivered_customer_date"].notnull().astype(int)
orders["delivery_time_days"] = (orders["order_delivered_customer_date"] - orders["order_purchase_timestamp"]).dt.days
orders["is_late"] = (orders["order_delivered_customer_date"] > orders["order_estimated_delivery_date"]).fillna(False).astype(int)
orders["shipping_window_days"] = (orders["shipping_limit_date"] - orders["order_purchase_timestamp"]).dt.days
orders["promised_delivery_days"] = (orders["order_estimated_delivery_date"] - orders["order_purchase_timestamp"]).dt.days
orders["approval_delay_days"] = (orders["order_approved_at"] - orders["order_purchase_timestamp"]).dt.days

print("\nGenerating product-related features...")
products["product_category_name"] = products["product_category_name"].fillna("unknown")
products["is_category_missing"] = (products["product_category_name"] == "unknown").astype(int)
products["product_volume_cm3"] = (
    products["product_length_cm"] * products["product_height_cm"] * products["product_width_cm"]
)
products["is_large_product"] = (products["product_weight_g"] > 10000) | (products["product_volume_cm3"] > 100000)

print("\nGenerating review and payment features...")
reviews["has_review"] = reviews["review_comment_message"].notnull().astype(int)
payments["payment_installments"] = payments["payment_installments"].fillna(0)
payments["payment_value"] = payments["payment_value"].fillna(0)

print("\nMerging all features into model-ready dataset...")
df = orders.merge(customers, on="customer_id", how="left")
df = df.merge(order_items, on="order_id", how="left")
df = df.merge(products, on="product_id", how="left")
df = df.merge(sellers, on="seller_id", how="left")
df = df.merge(
    payments.groupby("order_id").agg({
        "payment_value": "sum",
        "payment_installments": "sum"
    }).reset_index(),
    on="order_id", how="left"
)
df = df.merge(reviews[["order_id", "review_score", "has_review"]], on="order_id", how="left")

print("\nAdding order item count and price features...")
order_item_counts = order_items.groupby("order_id")["order_item_id"].max().reset_index()
order_item_counts.rename(columns={"order_item_id": "num_items"}, inplace=True)
df = df.merge(order_item_counts, on="order_id", how="left")

df = df.drop_duplicates(subset=["order_id"])
df["total_price"] = df["price"] + df["freight_value"]
df["log_distance_seller_customer"] = np.log1p(df["customer_seller_distance_km"])

print("\nFinal cleanup and target feature creation...")
df["delivery_time_days"] = df["delivery_time_days"].fillna(-1)
df["review_score"] = df["review_score"].fillna(0)
df["delivered_late"] = df["is_late"]

df.to_csv("../data/processed/olist_model_ready.csv", index=False)
print("\nFeature engineering completed and model-ready dataset saved.\n")
