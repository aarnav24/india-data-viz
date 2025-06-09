# India Census Data Visualization App

An interactive Streamlit web application for visualizing Indian census and infrastructure data by district and state.

## 📊 Overview

This application enables users to explore and analyze various demographic and infrastructure indicators across Indian districts and states using interactive maps. The data is presented in an easy-to-understand format with support for customized visual comparisons using Plotly.

## 🚀 Features

- Sidebar-based user interface
- Select any Indian state or view overall India
- Choose any two parameters (e.g., Population, Literacy, Internet Access) for comparison
- Visualize data on a map with:
  - **Size** representing the primary parameter
  - **Color** representing the secondary parameter
- Supports zoomed views for selected states
- Uses Plotly’s Mapbox for interactive map rendering

## 🗂️ Dataset

The data is sourced from a CSV file (`india.csv`) containing the following columns:

- **Geographic Info**: `State`, `District`, `Latitude`, `Longitude`
- **Demographics**: `Population`, `Male`, `Female`, `Literate`
- **Infrastructure**:
  - `Households_with_Internet`
  - `Housholds_with_Electric_Lighting`
  - `Urban_Households`
  - `LPG_or_PNG_Households`
  - `Households_with_Car_Jeep_Van`
  - `Ownership_Owned_Households`
  - Water sources (e.g., `Main_source_of_drinking_water_River_Canal_Households`)
  - Household sizes, education levels, etc.
  - `Total_Power_Parity`

## 🛠️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/india-census-viz.git
   cd india-census-viz
