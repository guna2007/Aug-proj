# Olist E-Commerce Data Pipeline

Delivering an end-to-end data pipeline and business analytics using the Olist dataset.

---

## Project Overview

- **Objective**: Understand and model delivery delays using the Olist Brazilian E-Commerce dataset.
- **Importance**: Provides insights into logistics performance, customer satisfaction, and business trends to inform operational decisions and future analytics (web dashboard).

Data source: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

---

## Repository Structure

- `data/raw/`: Original Kaggle CSVs
- `data/processed/`: Cleaned, merged, and staged data assets
- `scripts/`: Modular scripts for cleaning, feature engineering, EDA, and orchestration
- `reports/`: Auto-generated plots and summaries (created at runtime)
- `notebooks/`: Exploratory notebooks for ad hoc analyses
- `web_dashboard/`: Optional dashboard artifacts (to be expanded in Phase 5)

---

## Scripts Workflow

Primary pipeline entrypoint:

- `scripts/main_pipeline.py`: Orchestrates the full workflow end-to-end

Core steps (as executed by the pipeline):

- `scripts/data_cleaning.py`: Loads raw CSVs, normalizes columns, converts timestamps, handles nulls/duplicates, and saves `*_clean.csv` to `data/processed/`
- `scripts/data_validation.py`: Basic data integrity checks (types, ranges, required keys)
- `scripts/feature_engineering.py`: Merges entities, computes geo distances, delivery features, product metrics, and saves `data/processed/olist_model_ready.csv`
- `scripts/final_cleanup.py`: Removes redundant columns and saves `data/processed/final_ml_ready.csv`
- `scripts/eda_summary.py`, `scripts/eda_insights.py`, `scripts/eda_plots.py`: Exploratory summaries and figures
- `scripts/eda_business_needs.py`: Prepares the business-ready dataset `data/processed/eda_business_ready.csv`
- `scripts/eda_business_plots.py`: Generates strategic plots into `reports/business/*.png` (auto-creates directories)

Notes:

- Actual script names reflect the codebase (e.g., `eda_business_needs.py` produces the business-ready CSV).
- Plot scripts create directories under `reports/` if missing.

---

## How to Run the Pipeline

1. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
2. Run the full pipeline (from repo root or `scripts/`)

   ```bash
   # From repo root
   python scripts/main_pipeline.py

   # Or from scripts folder
   cd scripts && python main_pipeline.py
   ```

3. Outputs
   - Data: `data/processed/`
     - `olist_model_ready.csv` (feature-engineered)
     - `final_ml_ready.csv` (cleaned for ML)
     - `eda_business_ready.csv` (business-focused)
   - Reports: `reports/business/*.png`

Environment

- Python 3.x recommended
- Ensure raw CSVs are present in `data/raw/`

Run steps individually (optional)

```bash
python scripts/data_cleaning.py
python scripts/feature_engineering.py
python scripts/final_cleanup.py
python scripts/eda_business_needs.py
python scripts/eda_business_plots.py
```

---

## Phase Summary

- **Completed (August 2025)**: Data cleaning, feature engineering, EDA, business-focused datasets and plots
- **Next (September 2025)**: Web dashboard integration (Streamlit) using outputs in `data/processed/` and `reports/`

---

## Project Highlights

- **Business-first narrative**: KPIs for late deliveries, delays by region and category, and payment correlations
- **Modular pipeline**: Independent scripts orchestrated by a single entrypoint
- **Ready for dashboard**: Stable, documented outputs for seamless integration into a Streamlit app

---

## Usage Instructions

Clone and set up

```bash
git clone <your-repo-url>
cd olist_data_project
pip install -r requirements.txt
```

Run and explore

```bash
python scripts/main_pipeline.py
```

- Inspect processed datasets in `data/processed/`
- Review figures in `reports/business/`

Contribute

- Fork the repo, create a feature branch, and open a pull request
- Keep scripts modular and avoid hard-coding file system paths beyond `data/` and `reports/`

---

## Deliverables

- Final datasets
  - `data/processed/final_ml_ready.csv`
  - `data/processed/eda_business_ready.csv`
  - `data/processed/olist_model_ready.csv`
- Plots
  - `reports/business/*.png` (e.g., category late rate, delay by state, payment vs delay, monthly trend)

---

## Preparing for Phase 5: Web Dashboard

- Target framework: Streamlit
- Data inputs: `data/processed/eda_business_ready.csv`, `data/processed/final_ml_ready.csv`
- Visuals: Use pre-generated plots from `reports/business/` and add interactive charts (e.g., category/state filters)
- Suggested structure:
  - `web_dashboard/app.py` (new, Streamlit entrypoint)
  - `web_dashboard/assets/` for static assets

---

## Acknowledgments

- Olist Brazilian E-Commerce Dataset (Kaggle)

---

## License

Specify a license (e.g., MIT) if you intend to open source the project.
