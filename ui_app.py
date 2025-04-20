import streamlit as st
from sheet_connector import get_settings, write_results
from montecarlo_sim import run_simulation

st.set_page_config(layout="wide")
st.title("📈 Portfolio Retirement Optimizer")

with st.sidebar:
    st.header("Simulation Settings")
    inflation = st.number_input("Inflation Rate (%)", value=2.5)
    years = st.number_input("Years to Simulate", value=30)
    paths = st.number_input("Monte Carlo Paths", value=10000, step=1000)
    run_btn = st.button("Run Simulation")

if run_btn:
    settings = get_settings()
    results = run_simulation(settings, inflation/100, years, paths)
    write_results(results)
    st.success("Simulation complete!")
