
import streamlit as st
from sheet_connector import read_settings, write_results
import numpy as np

st.title("Portfolio Retirement Optimizer")

# Step 1: Read inputs from Google Sheets
settings = read_settings()
inflation = float(settings.get("Inflation (%)", 2.5)) / 100
target = float(settings.get("Target Real $ 2035", 6500000))
paths = int(settings.get("MC Paths", 10000))

# Step 2: Simulate Monte Carlo using dummy logic (placeholder)
initial_value = 1_000_000
mu, sigma = 0.07, 0.12
years = 10
results = []

for _ in range(paths):
    value = initial_value
    path = []
    for _ in range(years):
        value *= np.random.normal(1 + mu, sigma)
        path.append(value)
    results.append(path)

# Step 3: Aggregate percentiles
results = np.array(results)
percentiles = [5, 10, 25, 50, 75, 90]
table = []
for year in range(years):
    row = [year + 2025]
    for p in percentiles:
        row.append(np.percentile(results[:, year], p))
    table.append(row)

# Step 4: Output
st.subheader("Percentile Projections")
st.dataframe(table, use_container_width=True)

# Step 5: Save back to Google Sheets
write_results(table)
