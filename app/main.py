import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data, plot_boxplot, get_summary_table, plot_avg_metric_bar

st.set_page_config(page_title="Solar Insights Dashboard", layout="wide")

st.title("Solar Potential Comparison Dashboard")

# Sidebar for country selection
countries = ["Benin", "Sierra Leone", "Togo"]
selected_countries = st.sidebar.multiselect("Select countries to compare", countries, default=countries)

# Load data
data = load_data(selected_countries)

# Metric selection
metric = st.selectbox("Select a metric", ["GHI", "DNI", "DHI"])

# Boxplot section
st.subheader(f"{metric} Distribution (Boxplot)")
fig = plot_boxplot(data, metric)
st.pyplot(fig)

# Summary Table
st.subheader("Summary Statistics")
summary_df = get_summary_table(data)
st.dataframe(summary_df, use_container_width=True)

# Average Metric Bar Chart
st.subheader(f"Average {metric} by Country")
fig2 = plot_avg_metric_bar(data, metric)
st.pyplot(fig2)

