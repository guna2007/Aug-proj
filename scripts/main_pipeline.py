import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time
import importlib
from datetime import datetime


def print_header(title):
    print(f"\nStarting: {title}")

def print_success(title):
    print(f"Completed: {title}\n")

def print_error(title, error):
    print(f"Error in {title}: {error}\n")

def run_script(script_name, display_name):
    try:
        print_header(display_name)
        print(f"Running {script_name}.py...")
        module = importlib.import_module(script_name)
        importlib.reload(module)
        print_success(display_name)
        return True
    except Exception as e:
        print_error(display_name, e)
        print("Continuing to next step.")
        return False

def run_pipeline():
    """Run the full pipeline."""
    start_time = time.time()
    print(f"\nPipeline started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Executing all steps in sequence...\n")

    pipeline_steps = [
        ("data_cleaning", "Data Cleaning"),
        ("data_validation", "Data Validation"),
        ("feature_engineering", "Feature Engineering"),
        ("final_cleanup", "Final Cleanup"),
        ("eda_summary", "EDA Summary"),
        ("eda_insights", "EDA Insights"),
        ("eda_plots", "EDA Plots"),
        ("eda_business_needs", "EDA Business Needs"),
        ("eda_business_plots", "EDA Business Plots")
    ]

    completed_steps = []
    for script_name, display_name in pipeline_steps:
        if run_script(script_name, display_name):
            completed_steps.append(display_name)

    end_time = time.time()
    duration = end_time - start_time

    print(f"\nPipeline completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total execution time: {duration:.2f} seconds ({duration/60:.2f} minutes)\n")

    print("Completed steps:")
    for step in completed_steps:
        print(f"- {step}")

    if len(completed_steps) < len(pipeline_steps):
        print("\nSome steps failed. Review the error messages above.")
    else:
        print("\nAll steps executed successfully.")

if __name__ == "__main__":
    run_pipeline()
