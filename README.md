# Olist E‑Commerce Data Pipeline

Delivering an end-to-end data pipeline and business analytics using the Olist Brazilian E‑Commerce dataset.

---

## Project Overview

- **Objective**: Understand and model delivery delays using the Olist Brazilian E‑Commerce dataset.
- **Importance**: Insights into logistics performance, customer satisfaction, and business trends to inform operations and future analytics.
- **Business Context**: The pipeline cleans, validates, and engineers ML‑ready features (delivery times, geo distances, shipping costs) to support predictive modeling of late deliveries.

Data source: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

---

## Key Outputs

- **ML-Ready Dataset** → Final feature-engineered dataset prepared for delivery delay prediction.
- **Business-Ready Dataset** → Cleaned and structured dataset optimized for BI and analytics use.
- **Visualizations** → Core business plots highlighting sales performance, customer satisfaction, and delivery efficiency.

📌 Note: Due to file size, the final CSVs are not stored in this repo. They are shared alongside the month-end LinkedIn project post.

---

## Repository Structure

<pre>
olist_data_project/
├─ data/
│  └─ raw/                   # Original Kaggle CSVs (required input)
├─ docs/
│  └─ data_dictionary.md     # Data dictionary for raw and processed fields
├─ notebooks/                # Exploratory notebooks (Phase1–4, etc.)
├─ reports/                  # Generated plots and summaries (created at runtime)
├─ scripts/                  # Modular pipeline scripts
│  ├─ data_cleaning.py
│  ├─ data_validation.py
│  ├─ feature_engineering.py
│  ├─ final_cleanup.py
│  ├─ eda_summary.py
│  ├─ eda_insights.py
│  ├─ eda_plots.py
│  ├─ eda_business_needs.py
│  ├─ eda_business_plots.py
│  └─ main_pipeline.py       # Orchestration entrypoint
├─ web_dashboard/            # Static dashboard (HTML/CSS/JS)
│  ├─ index.html
│  ├─ script.js
│  ├─ styles.css
│  ├─ profile-pic.jpeg
│  └─ graphs/
│     ├─ basic_plots/
│     └─ business/
├─ LICENSE
├─ README.md
└─ requirements.txt
</pre>

Notes:

- data/processed/ is created at runtime by the pipeline.
- reports/ subfolders (e.g., reports/business/) are auto-created by plotting scripts.

---

## Scripts Workflow

Primary entrypoint:

- `scripts/main_pipeline.py` — Orchestrates the full workflow end‑to‑end.

Core steps:

- `scripts/data_cleaning.py` — Load raw CSVs, standardize columns, convert timestamps, handle nulls/duplicates; writes cleaned outputs to data/processed/.
- `scripts/data_validation.py` — Integrity checks on types, ranges, and required keys before downstream processing.
- `scripts/feature_engineering.py` — Merge entities, compute geo distances, delivery features, product metrics; writes data/processed/olist_model_ready.csv.
- `scripts/final_cleanup.py` — Drop redundant columns, finalize schema; writes data/processed/final_ml_ready.csv.
- `scripts/eda_summary.py`, `scripts/eda_insights.py`, `scripts/eda_plots.py` — Exploratory summaries and figures.
- `scripts/eda_business_needs.py` — Build business‑focused dataset; writes data/processed/eda_business_ready.csv.
- `scripts/eda_business_plots.py` — Generate strategic plots under reports/business/\*.png (auto‑creates directories).

---

## How to Run

**Prerequisites**

- Python 3.x
- Kaggle CSVs present in data/raw/

**Install dependencies**

```bash
pip install -r requirements.txt
```

**Run the full pipeline (from repo root)**

```bash
python scripts/main_pipeline.py
```

**Outputs:**

Data (created in data/processed/)

- olist_model_ready.csv (feature‑engineered)
- final_ml_ready.csv (cleaned for ML)
- eda_business_ready.csv (business‑focused)

Reports

- reports/business/\*.png (plots auto‑created)

**Run steps individually (optional)**

```bash
python scripts/data_cleaning.py
python scripts/data_validation.py
python scripts/feature_engineering.py
python scripts/final_cleanup.py
python scripts/eda_summary.py
python scripts/eda_insights.py
python scripts/eda_plots.py
python scripts/eda_business_needs.py
python scripts/eda_business_plots.py
```

---

## Phase Summary

- **Completed (Aug 2025):** Data cleaning, validation, feature engineering, EDA, business datasets, and plots.
- Web dashboard (static): HTML/CSS/JS app reads outputs from data/processed/ and reports/.

---

## Data Dictionary

A complete data dictionary for raw and processed datasets is available at [docs/data_dictionary.md](docs/data_dictionary.md).

---

## Web Dashboard

- **Current implementation:** Static HTML/CSS/JS located in web_dashboard/.
- **How to view:** Open web_dashboard/index.html in a browser.
- **Assets:** Pre-generated plots available under web_dashboard/graphs/ and reports/business/.
- **Future enhancement:**
  - Explore a Streamlit version using data/processed/ datasets and reports/business/ visuals for interactivity.

---

## What I Learned

- **Data Engineering Foundations** – Cleaning, merging, and transforming multiple datasets into ML‑ready formats.
- **Feature Engineering for Business** – Extracting signals (weight, distance, dimensions, cost) that affect delivery performance.
- **EDA & Visualization** – Plots for business storytelling (delays, logistics patterns, customer impact).
- **Frontend Basics** – Built a static dashboard with HTML/CSS/JS.
- **Pipeline Thinking** – From ad‑hoc analysis to a repeatable, end‑to‑end pipeline.

---

## Deliverables

- data/processed/final_ml_ready.csv
- data/processed/eda_business_ready.csv
- data/processed/olist_model_ready.csv
- Plots: reports/business/\*.png (e.g., category late rate, delay by state, payment vs delay, monthly trend)

(See “Key Outputs” for high‑level summary and note on file size.)

---

## Next Steps

- Build a model to predict delivery delays using engineered features (dimensions, weight, distance, shipping cost).
- Expose predictions via an API and enhance the dashboard with interactivity.
- Add “what‑if” simulations (e.g., cost/distance trade‑offs).

---

## License

📄 This project is licensed under the MIT License — see the LICENSE file for details.

---

## 👨‍💻 Author

[L. Guna] — Trinity Developer, Data Pipeline (Aug 2025)
GitHub: [@guna2007](https://github.com/guna2007)

---

## Final Thoughts

This project demonstrates a full data pipeline lifecycle: raw data ingestion and cleaning, feature engineering, business analytics, and dashboard readiness—built with modularity, iterative debugging, and business impact in mind.

---

## Repository Structure

- `data/raw/`: Original Kaggle CSVs
- `data/processed/`: Cleaned, merged, and staged data assets
- `scripts/`: Modular scripts for cleaning, feature engineering, EDA, and orchestration
- `reports/`: Auto-generated plots and summaries (created at runtime)
- `notebooks/`: Exploratory notebooks for ad hoc analyses
- `web_dashboard/`: Optional dashboard artifacts (to be expanded in Phase 5)
- `docs/`: Documentation, including the data dictionary

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

- **Completed (August 2025)**: Data cleaning, feature engineering, EDA, business-focused datasets and plots,Web dashboard integration (Streamlit) using outputs in `data/processed/` and `reports/`

## Project Highlights

**Business-first narrative**: KPIs for late deliveries, delays by region and category, and payment correlations
**Modular pipeline**: Independent scripts orchestrated by a single entrypoint
**Ready for dashboard**: Stable, documented outputs for seamless integration into a Streamlit app
**Memory & Size Optimization**: Reduced dataset size from ~120MB raw Kaggle CSVs to ~45MB ML-ready processed data
**Performance Metrics**:

- Rows processed: ~100,000 orders
- Columns engineered: ~20 raw → 42 engineered features
- Business insights: delivery delays, category impact, regional delays

---

## What I Learned

- **Data Engineering Foundations** – How to clean, merge, and transform multiple noisy datasets into structured, ML-ready formats.
- **Feature Engineering for Business** – Extracting real-world signals (weight, distance, dimensions, cost) that impact delivery performance.
- **EDA & Visualization** – Designing plots not just for exploration, but for business storytelling (delays, logistics patterns, customer impact).
- **Mistakes & Fixes** – Over-engineering early scripts, handling missing values incorrectly, and redundant preprocessing taught me the importance of modularity and iterative debugging.
- **Frontend Development** – Built a static dashboard by learning HTML/CSS/JS from scratch, with my AI assistant as a co-developer.
- **Pipeline Thinking** – Shifted mindset from just “analysis” to building a repeatable, end-to-end pipeline that outputs consistent business-ready datasets.

## Data Dictionary

A complete data dictionary for raw and processed datasets is available [here](docs/data_dictionary.md).

---

## Usage Instructions

Clone and set up

```bash
git clone https://github.com/guna2007/Aug-proj.git
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

Final datasets

- `data/processed/final_ml_ready.csv`
- `data/processed/eda_business_ready.csv`
- `data/processed/olist_model_ready.csv`
  Plots
- `reports/business/*.png` (e.g., category late rate, delay by state, payment vs delay, monthly trend)

---

## Trinity Plan (Aug 2025)

**Theme:** Real-world data prep, cleaning, and visualization.

- ✅ Built an automated pipeline: raw → ML-ready CSVs.
- ✅ Conducted EDA + created business-ready datasets & plots.
- ✅ Developed static web dashboard (HTML/CSS/JS).
- ✅ Reduced dataset size: 120MB raw → 45MB processed.
- 🎯 Deliverables: `final_ml_ready.csv`, `eda_business_ready.csv`, reports/business/\*.png

---

## Next Steps (Sept 2025)

- Build machine learning model to **predict delivery delays** using ML-ready features (dimensions, weight, distance, shipping cost, etc.).
- Expose predictions through a **REST API + Good dashboard**.
- Enable businesses to simulate "what-if" scenarios (e.g., cost/distance trade-offs).

**Real-world factors:** weight, dimensions, distance, cost → features engineered → predictive model.

---

## Phase 5: Web Dashboard

- Target framework: Streamlit
- Data inputs: `data/processed/eda_business_ready.csv`, `data/processed/final_ml_ready.csv`
- Visuals: Use pre-generated plots from `reports/business/` and add interactive charts (e.g., category/state filters)
- Suggested structure:
  - `web_dashboard/app.py` (new, Streamlit entrypoint)
  - `web_dashboard/assets/` for static assets

---

## License

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

[L.Guna] - Trinity Developer Data Pipeline August 2025

GitHub: [@guna2007](https://github.com/guna2007)
Project Link: [Aug-Project](https://github.com/guna2007/Aug-Project)

## 🙏 Acknowledgments

- Trinity Developer Foundations – For the structured learning path
- Olist Brazilian E-Commerce Dataset (Kaggle)
- pandas, numpy – For robust data wrangling and analysis
- matplotlib, seaborn – For beautiful visualizations
- Python Community, Jupyter – For amazing tools and resources

## 🙌 Final Thoughts

This project demonstrates the full lifecycle of a real-world data pipeline: from raw data ingestion and cleaning, through feature engineering and business analytics, to web dashboard integration and predictive modeling readiness. The journey involved not just technical skills, but also iterative debugging, design thinking, and a focus on business impact.

If you're a recruiter, data scientist, or engineer, this repository is designed to showcase practical skills, modular code, and a clear roadmap for future development. Contributions and feedback are welcome!
