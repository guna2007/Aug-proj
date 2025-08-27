# Olist E‑Commerce Data Pipeline

Delivering an end-to-end data pipeline and business analytics using the Olist Brazilian E‑Commerce dataset.

---

## Project Overview

- **Objective**: Understand and model delivery delays using the Olist Brazilian E-Commerce dataset.
- **Importance**: Provide actionable insights into logistics performance, customer satisfaction, and business trends to inform operations and future analytics.
- **Business Context**: The pipeline cleans, validates, and engineers ML-ready features (delivery times, geo distances, shipping costs) to support predictive modeling of late deliveries.
- **Deliverable**: A deployed [Olist Dashboard](https://olist-dashboard.vercel.app/) showcasing key business visualizations and insights generated from the processed pipeline outputs.
- **Data Source**: [Olist Brazilian E-Commerce Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

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

- `scripts/main_pipeline.py`: Orchestrates the full workflow end-to-end
- `scripts/data_cleaning.py`: Loads raw CSVs, normalizes columns, converts timestamps, handles nulls/duplicates, and saves `*_clean.csv` to `data/processed/`
- `scripts/data_validation.py`: Basic data integrity checks (types, ranges, required keys)
- `scripts/feature_engineering.py`: Merges entities, computes geo distances, delivery features, product metrics, and saves `data/processed/olist_model_ready.csv`
- `scripts/final_cleanup.py`: Removes redundant columns and saves `data/processed/final_ml_ready.csv`
- `scripts/eda_summary.py`, `scripts/eda_insights.py`, `scripts/eda_plots.py`: Exploratory summaries and figures
- `scripts/eda_business_needs.py`: Prepares the business-ready dataset `data/processed/eda_business_ready.csv`
- `scripts/eda_business_plots.py`: Generates strategic plots into `reports/business/*.png` (auto-creates directories)

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

- Data: `data/processed/`
  - `olist_model_ready.csv` (feature-engineered)
  - `final_ml_ready.csv` (cleaned for ML)
  - `eda_business_ready.csv` (business-focused)
- Reports: `reports/business/*.png`

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

## Key Outputs & Deliverables

- **ML-Ready Dataset**: Final feature-engineered dataset for delivery delay prediction
- **Business-Ready Dataset**: Cleaned and structured dataset for BI/analytics
- **Visualizations**: Core business plots (sales, customer satisfaction, delivery efficiency)
- **Plots**: `reports/business/*.png` (e.g., category late rate, delay by state, payment vs delay, monthly trend)

📌 Note: Due to file size, the final CSVs are not stored in this repo. They are shared alongside the month-end LinkedIn project post.

---

## Project Highlights

- **Business-first narrative**: KPIs for late deliveries, delays by region and category, and payment correlations
- **Modular pipeline**: Independent scripts orchestrated by a single entrypoint
- **Ready for dashboard**: Stable, documented outputs for seamless integration into a Streamlit app
- **Memory & Size Optimization**: Reduced dataset size from ~120MB raw Kaggle CSVs to ~45MB ML-ready processed data
- **Performance Metrics**:
  - Rows processed: ~100,000 orders
  - Columns engineered: ~20 raw → 42 engineered features
  - Business insights: delivery delays, category impact, regional delays

---

## Phase Summary & Trinity Plan

- **Completed (Aug 2025):** Data cleaning, validation, feature engineering, EDA, business datasets, and plots
- ✅ Built an automated pipeline: raw → ML-ready CSVs
- ✅ Conducted EDA + created business-ready datasets & plots
- ✅ Developed static web dashboard (HTML/CSS/JS)
- ✅ Reduced dataset size: 120MB raw → 45MB processed
- 🎯 Deliverables: `final_ml_ready.csv`, `eda_business_ready.csv`, reports/business/\*.png

---

## Web Dashboard

- **Current implementation:** Static HTML/CSS/JS located in web_dashboard/
- **How to view:** Open web_dashboard/index.html in a browser
- **Assets:** Pre-generated plots under web_dashboard/graphs/ and reports/business/

---

## Data Dictionary

A complete data dictionary for raw and processed datasets is available at [docs/data_dictionary.md](docs/data_dictionary.md).

---

## What I Learned

- **Data Engineering Foundations**: Cleaning, merging, and transforming multiple noisy datasets into structured, ML-ready formats
- **Feature Engineering for Business**: Extracting real-world signals (weight, distance, dimensions, cost) that impact delivery performance
- **EDA & Visualization**: Designing plots for business storytelling (delays, logistics patterns, customer impact)
- **Mistakes & Fixes**: Over-engineering early scripts, handling missing values incorrectly, and redundant preprocessing taught the importance of modularity and iterative debugging
- **Frontend Development**: Built a static dashboard by learning HTML/CSS/JS from scratch, with my AI assistant as a co-developer
- **Pipeline Thinking**: Shifted mindset from just “analysis” to building a repeatable, end-to-end pipeline that outputs consistent business-ready datasets

---

## Next Steps

- Build a machine learning model to predict delivery delays using engineered features (dimensions, weight, distance, shipping cost, etc.)
- Expose predictions through a REST API and enhance the dashboard with interactivity
- Enable businesses to simulate "what-if" scenarios (e.g., cost/distance trade-offs)

---

## Usage & Contribution

**Clone and set up**

```bash
git clone https://github.com/guna2007/Aug-proj.git
cd olist_data_project
pip install -r requirements.txt
```

**Run and explore**

```bash
python scripts/main_pipeline.py
```

- Inspect processed datasets in `data/processed/`
- Review figures in `reports/business/`

**Contribute**

- Fork the repo, create a feature branch, and open a pull request
- Keep scripts modular and avoid hard-coding file system paths beyond `data/` and `reports/`

---

## License

📄 This project is licensed under the MIT License — see the LICENSE file for details.

---

## Author

[L. Guna] — Trinity Developer, Data Pipeline (Aug 2025)
GitHub: [@guna2007](https://github.com/guna2007)
Project Link: [Aug-Project](https://github.com/guna2007/Aug-Project)

---

## Acknowledgments

- Trinity Developer Foundations – For the structured learning path
- Olist Brazilian E-Commerce Dataset (Kaggle)
- pandas, numpy – For robust data wrangling and analysis
- matplotlib, seaborn – For beautiful visualizations
- Python Community, Jupyter – For amazing tools and resources

---

## Final Thoughts

This project demonstrates the full lifecycle of a real-world data pipeline: from raw data ingestion and cleaning, through feature engineering and business analytics, to web dashboard integration and predictive modeling readiness. The journey involved not just technical skills, but also iterative debugging, design thinking, and a focus on business impact.

If you're a recruiter, data scientist, or engineer, this repository is designed to showcase practical skills, modular code, and a clear roadmap for future development. Contributions and feedback are welcome!
