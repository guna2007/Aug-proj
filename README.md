# 🛒 Olist E-Commerce Data Explorer

An end-to-end data project using the Olist Brazilian E-Commerce Dataset (from Kaggle), focusing on:

- 🔍 Real-world data cleaning and integration
- 🛠️ Feature engineering for insights
- 📊 Exploratory Data Analysis (EDA) with visualizations
- 🌐 Optional web dashboard to present results

---

## 📦 Dataset

[🔗 Olist Dataset on Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

The dataset contains:

- Orders and deliveries
- Customer info
- Products and categories
- Reviews
- Payment details

---

## 📂 Project Structure

| Module            | Description                                                  |
| ----------------- | ------------------------------------------------------------ |
| `data/raw/`       | Original unmodified CSV files                                |
| `data/processed/` | Cleaned, merged, transformed data                            |
| `scripts/`        | All core data logic (cleaning, features, validation)         |
| `notebooks/`      | EDA and visual exploration using pandas, seaborn, matplotlib |
| `web_dashboard/`  | Dashboard to present results interactively                   |

---

## 🧱 Project Phases

1. **Data Cleaning**: nulls, duplicates, formats, consistency
2. **Feature Engineering**: new metrics like delays, repeat customers, revenue
3. **Validation**: basic range and logic checks
4. **EDA**: sales trends, delivery performance, state-wise performance
5. **Web Dashboard**: Present graphs and insights (optional)

---

## 🚀 Tools Used

- Python, Pandas, NumPy
- Matplotlib, Seaborn
- Jupyter Notebooks
- HTML/CSS (optional dashboard)

---

## ✅ Author

Guna – B.Tech CSE (AI) | Data & Web Dev Enthusiast  
🔗 [LinkedIn](https://linkedin.com/in/guna-lankalapalli)  
📁 Part of the **Trinity Plan – August 2025 Project**

CUSTOMERS —(1:M)— ORDERS —(1:M)— ORDER_ITEMS —(M:1)— PRODUCTS
|
|——(1:M)— PAYMENTS
|——(1:M)— REVIEWS

SELLERS —(1:M)— ORDER_ITEMS  
CUSTOMERS —(1)— GEODATA (via zip code)
SELLERS —(1)— GEODATA (via zip code)

## 📄 Phase 1: Dataset Overview & Schema

This project uses the Olist Brazilian E-Commerce dataset with 9 interconnected CSVs.

### Main Tables:

- `orders`: Core table listing each order
- `order_items`: Products per order
- `payments`: Payment methods and amounts
- `reviews`: Customer feedback
- `products`: Product categories and metadata
- `customers`, `sellers`: Location-based info
- `geolocation`: Lat/lon data (for distance calculation)
- `product_category_name_translation`: Mapping Portuguese to English

### Relationships:

- One customer → many orders
- One order → many items, payments, reviews
- One product → many items
- One seller → many items

## 📘 Schema Mapping Overview

Before merging datasets in the Olist project, it's essential to understand the relationships between tables. This schema mapping serves as a blueprint for how entities connect, ensuring accurate joins and a clean data pipeline.

### 🧱 Core Entities

| Entity                 | Primary Key              | Description                                                   |
| ---------------------- | ------------------------ | ------------------------------------------------------------- |
| `orders`               | `order_id`               | Central table — each row represents a customer order          |
| `customers`            | `customer_id`            | Contains customer demographic and location info               |
| `sellers`              | `seller_id`              | Contains seller details and location                          |
| `products`             | `product_id`             | Product metadata including category                           |
| `order_items`          | `order_id`, `product_id` | Links orders to products and sellers                          |
| `payments`             | `order_id`               | Payment method and transaction amount                         |
| `reviews`              | `order_id`               | Customer review score and comment                             |
| `category_translation` | `product_category_name`  | Maps Portuguese category names to English                     |
| `geolocation`          | `zip_code_prefix`        | Location data for customers and sellers (not directly linked) |

### 🔗 Key Relationships

| Relationship                        | Type        | Join Key                |
| ----------------------------------- | ----------- | ----------------------- |
| `orders` → `customers`              | Many-to-One | `customer_id`           |
| `orders` → `order_items`            | One-to-Many | `order_id`              |
| `order_items` → `products`          | Many-to-One | `product_id`            |
| `order_items` → `sellers`           | Many-to-One | `seller_id`             |
| `orders` → `payments`               | One-to-One  | `order_id`              |
| `orders` → `reviews`                | One-to-One  | `order_id`              |
| `products` → `category_translation` | Many-to-One | `product_category_name` |

### 🧠 Why Schema Mapping Matters

- Prevents incorrect joins and data duplication
- Guides feature engineering and model design
- Ensures scalable and maintainable data pipelines
- Helps identify missing or incomplete data early

### 🛠️ Merge Strategy

Start with `orders` as the base table and progressively join:

1. `customers` via `customer_id`
2. `order_items` via `order_id`
3. `products` and `sellers` via `product_id` and `seller_id`
4. `payments` and `reviews` via `order_id`
5. `category_translation` via `product_category_name`

Use **left joins** to retain all orders, even if some have missing reviews or payments.

---

# 📦 Delivery Delay Prediction – Feature Overview

This project uses the Olist dataset to predict whether an order will be delivered late (i.e., after the estimated delivery date). The target column is:

- `delivered_late`:
  - `1` if `order_delivered_customer_date` > `order_estimated_delivery_date`
  - `0` otherwise

## ✅ Selected Features

### 🕒 Time Features

- `order_purchase_timestamp`
- `order_approved_at`
- `order_estimated_delivery_date`
- `approval_delay` = `order_approved_at` − `order_purchase_timestamp`
- `estimated_delivery_days` = `order_estimated_delivery_date` − `order_purchase_timestamp`
- `purchase_day_of_week` = weekday of `order_purchase_timestamp`
- `purchase_month` = month of `order_purchase_timestamp`

### 🌍 Location Features

- `customer_state`
- `seller_state`
- `is_same_state` = 1 if seller and customer are in same state

### 📦 Product Features

- `product_category_name`
- `product_weight_g`
- `product_length_cm`
- `product_height_cm`
- `product_width_cm`
- `product_volume_cm3` = length × width × height

### 🛍️ Order Item Features

- `price`
- `freight_value`
- `number_of_items` (grouped by `order_id`)
- `freight_ratio` = freight_value / price

### 💳 Payment Features

- `payment_type`
- `payment_installments`
- `payment_value`
