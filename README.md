# Solar Challenge Week 1

This repository contains a Streamlit dashboard for analyzing and comparing solar irradiance data across different countries (Benin, Sierra Leone, and Togo). The dashboard provides interactive visualizations and statistical analysis of Global Horizontal Irradiance (GHI), Direct Normal Irradiance (DNI), and Diffuse Horizontal Irradiance (DHI) metrics.

## Features

- Interactive country selection
- Dynamic metric selection (GHI, DNI, DHI)
- Boxplot visualization of irradiance distribution
- Summary statistics table
- Average irradiance comparison bar chart
- Responsive and user-friendly interface

## Project Structure

```
├── app/
│   ├── main.py          # Main Streamlit application
│   └── utils.py         # Utility functions for data processing and visualization
├── data/                # Data directory containing country-specific CSV files
├── dashboard_screenshots/  # Screenshots of the dashboard
├── .github/
│   └── workflows/
│       └── ci.yml       # GitHub Actions CI configuration
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

## Environment Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - Unix/MacOS:
     ```bash
     source venv/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Dashboard

1. Navigate to the app directory:
   ```bash
   cd app
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```

3. The dashboard will open in your default web browser at `http://localhost:8501`

## Usage Guide

1. **Country Selection**
   - Use the sidebar to select one or more countries to compare
   - Default selection includes all available countries

2. **Metric Selection**
   - Choose between GHI, DNI, or DHI metrics using the dropdown menu
   - All visualizations will update automatically based on your selection

3. **Visualizations**
   - Boxplot: Shows the distribution of the selected metric across countries
   - Summary Statistics: Displays mean, median, and standard deviation for all metrics
   - Bar Chart: Compares average values of the selected metric across countries

## Development Process

1. **Data Processing**
   - Data is loaded from country-specific CSV files
   - The `load_data` function in `utils.py` handles data loading and preprocessing
   - Data is combined and prepared for visualization

2. **Visualization Components**
   - Boxplot visualization (`plot_boxplot`): Shows distribution of irradiance metrics
   - Summary statistics (`get_summary_table`): Calculates key statistical measures
   - Bar chart (`plot_avg_metric_bar`): Compares average values across countries

3. **Dashboard Structure**
   - Main layout is defined in `main.py`
   - Interactive elements are implemented using Streamlit widgets
   - Visualizations are dynamically updated based on user selections
