import os
import pandas as pd

def load_processed_data():
    print("\nLoading cleaned CSV files from processed directory...")
    base_path = os.path.join(os.path.dirname(__file__), "..", "data", "processed")
    files = [
        "order_clean.csv",
        "customer_clean.csv",
        "order_item_clean.csv",
        "product_clean.csv",
        "translation_clean.csv",
        "seller_clean.csv",
        "order_payment_clean.csv",
        "order_review_clean.csv",
        "geolocation_clean.csv"
    ]

    dfs = {}
    for file in files:
        path = os.path.join(base_path, file)
        if os.path.exists(path):
            name = file.replace("_clean.csv", "")
            dfs[name] = pd.read_csv(path)
            print(f"Loaded: {file}")
        else:
            print(f"Missing processed file: {file}")
    return dfs

def check_nulls(dfs):
    print("\nChecking for null values in each dataframe...")
    print("\nNull Value Report:")
    for name, df in dfs.items():
        nulls = df.isnull().sum().sum()
        if nulls > 0:
            print(f"{name}: {nulls} null values present")
        else:
            print(f"{name}: No null values")

def check_duplicates(dfs):
    print("\nChecking for duplicate rows in each dataframe...")
    print("\nDuplicate Rows Report:")
    for name, df in dfs.items():
        dups = df.duplicated().sum()
        if dups > 0:
            print(f"{name}: {dups} duplicate rows")
        else:
            print(f"{name}: No duplicates")

def check_unique_ids(dfs):
    print("\nChecking uniqueness of key ID columns...")
    print("\nID Uniqueness Report:")
    if "order" in dfs:
        unique_orders = dfs["order"]["order_id"].is_unique
        print("order_id unique:", "Yes" if unique_orders else "No")

    if "customer" in dfs:
        unique_customers = dfs["customer"]["customer_id"].is_unique
        print("customer_id unique:", "Yes" if unique_customers else "No")

    if "seller" in dfs:
        unique_sellers = dfs["seller"]["seller_id"].is_unique
        print("seller_id unique:", "Yes" if unique_sellers else "No")

def check_expected_columns(dfs):
    print("\nValidating expected columns in each dataframe...")
    print("\nColumn Validation Report:")
    expected = {
        "order": ['order_id','customer_id','order_status','order_purchase_timestamp',
                  'order_approved_at','order_delivered_carrier_date',
                  'order_delivered_customer_date','order_estimated_delivery_date'],
        "customer": ['customer_id','customer_unique_id','customer_zip_code_prefix',
                     'customer_city','customer_state'],
        "order_item": ['order_id','order_item_id','product_id','seller_id','shipping_limit_date',
                       'price','freight_value'],
        "product": ['product_id','product_category_name','product_name_lenght',
                    'product_description_lenght','product_photos_qty',
                    'product_weight_g','product_length_cm','product_height_cm',
                    'product_width_cm'],
        "seller": ['seller_id','seller_zip_code_prefix','seller_city','seller_state'],
        "order_payment": ['order_id','payment_sequential','payment_type',
                          'payment_installments','payment_value'],
        "order_review": ['review_id','order_id','review_score','review_comment_title',
                         'review_comment_message','review_creation_date','review_answer_timestamp'],
        "geolocation": ['geolocation_zip_code_prefix','geolocation_lat','geolocation_lng',
                        'geolocation_city','geolocation_state']
    }

    for name, cols in expected.items():
        if name in dfs:
            missing = set(cols) - set(dfs[name].columns)
            if missing:
                print(f"{name}: Missing columns -> {missing}")
            else:
                print(f"{name}: All expected columns present")

dfs = load_processed_data()
if dfs:
    check_nulls(dfs)
    check_duplicates(dfs)
    check_unique_ids(dfs)
    check_expected_columns(dfs)
    print("\nValidation checks completed.\n")
else:
    print("\nNo processed files found. Run cleaning.py first.\n")
