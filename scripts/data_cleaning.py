import numpy as np
import pandas as pd
import os

def load_raw_data():
    print("\nLoading raw CSV files from disk...")
    base_path = os.path.join(os.path.dirname(__file__), "..", "data", "raw")
    files = {
        "order": "olist_orders_dataset.csv",                         
        "customer": "olist_customers_dataset.csv",                   
        "order_item": "olist_order_items_dataset.csv",              
        "product": "olist_products_dataset.csv",                     
        "translation": "product_category_name_translation.csv",     
        "seller": "olist_sellers_dataset.csv",                       
        "order_payment": "olist_order_payments_dataset.csv",         
        "order_review": "olist_order_reviews_dataset.csv",           
        "geolocation": "olist_geolocation_dataset.csv",              
    }

    dfs = {}
    for name, file in files.items():
        full_path = os.path.join(base_path, file)
        if os.path.exists(full_path):
            dfs[name] = pd.read_csv(full_path)
            print(f"Loaded {file} → {dfs[name].shape[0]} rows, {dfs[name].shape[1]} cols")
        else:
            print(f"File not found: {full_path}")
    return dfs

def normalize_columns(dfs):
    print("\nNormalizing column names across all dataframes...")
    for name, df in dfs.items():
        df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")
    return dfs

def convert_datetime_columns(dfs):
    print("\nConverting date columns to datetime format...")
    date_cols = {
        'order': ['order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date',
                  'order_delivered_customer_date', 'order_estimated_delivery_date'],
        'order_review': ['review_creation_date', 'review_answer_timestamp']
    }

    for df, col_list in date_cols.items(): 
        for col in col_list:
            dfs[df][col] = pd.to_datetime(dfs[df][col], errors="coerce")
    return dfs

def handle_missing_values(dfs):
    print("\nHandling missing values in key columns...")
    if "order" in dfs:
        dfs["order"].dropna(subset=["order_id", "customer_id"], inplace=True)

    if "product" in dfs:
        dfs["product"]["product_category_name"] = dfs["product"]["product_category_name"].fillna("unknown")
    
    if "order_review" in dfs:
        dfs["order_review"]["review_comment_message"] = dfs["order_review"]["review_comment_message"].fillna("")
    
    return dfs

def remove_duplicates(dfs):
    print("\nRemoving duplicate rows from all dataframes...")
    for name, df in dfs.items():
        initial = len(df)
        df.drop_duplicates(inplace=True)
        final = len(df)
        print(f"{initial-final} rows removed from {name}")
    return dfs

def save_cleaned_files(dfs):
    print("\nSaving cleaned dataframes to processed directory...")
    processed_path = os.path.join(os.path.dirname(__file__), "..", "data", "processed")
    
    # Create the processed directory if it doesn't exist
    os.makedirs(processed_path, exist_ok=True)

    for name, df in dfs.items():
        df.to_csv(os.path.join(processed_path, f"{name}_clean.csv"), index=False)
        print(f"Saved: {name}_clean.csv")


# pipeline
dfs = load_raw_data()
dfs = normalize_columns(dfs)
dfs = convert_datetime_columns(dfs)
dfs = handle_missing_values(dfs)
dfs = remove_duplicates(dfs)
save_cleaned_files(dfs)
print("\nCleaning pipeline completed successfully.\n")
