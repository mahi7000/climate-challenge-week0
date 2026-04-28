import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="COP32 Climate Dashboard", layout="wide")

st.title("Climate Analytics: COP32 Regional Dashboard")

# --- DATA LOADING ---
@st.cache_data
def load_data():
    # Path to your cleaned data folder
    data_path = "data/"
    files = [f for f in os.listdir(data_path) if f.endswith('_clean.csv')]
    df_list = []
    for file in files:
        temp_df = pd.read_csv(os.path.join(data_path, file))
        # Ensure Date is datetime
        temp_df['Date'] = pd.to_datetime(temp_df['Date'])
        df_list.append(temp_df)
    return pd.concat(df_list)

try:
    df = load_data()

    # --- SIDEBAR FILTERS ---
    st.sidebar.header("Filter Options")
    
    countries = st.sidebar.multiselect(
        "Select Countries", 
        options=df['Country'].unique(), 
        default=df['Country'].unique()[:1]
    )
    
    year_range = st.sidebar.slider(
        "Year Range", 
        int(df['Date'].dt.year.min()), 
        int(df['Date'].dt.year.max()), 
        (2015, 2026)
    )

    # --- FILTER LOGIC ---
    filtered_df = df[
        (df['Country'].isin(countries)) & 
        (df['Date'].dt.year >= year_range[0]) & 
        (df['Date'].dt.year <= year_range[1])
    ]

    # --- VISUALIZATIONS ---
    st.subheader("Temperature Trends (What is Changing?)")
    if not filtered_df.empty:
        # Create a 12-month rolling average for the dashboard to show the "Trend"
        filtered_df = filtered_df.sort_values(['Country', 'Date'])
        filtered_df['T2M_Rolling'] = filtered_df.groupby('Country')['T2M'].transform(lambda x: x.rolling(window=30).mean())
        
        fig = px.line(filtered_df, x='Date', y='T2M_Rolling', color='Country',
                      title="30-Day Rolling Average Temperature",
                      labels={'T2M_Rolling': 'Temp (°C)', 'Date': 'Timeline'})
        st.plotly_chart(fig, use_container_width=True)
        
        # Add a quick metric for the "Evidence Ladder"
        st.subheader("Regional Vulnerability Quick Stats")
        col1, col2 = st.columns(2)
        with col1:
            avg_temp = filtered_df['T2M'].mean()
            st.metric("Avg Period Temp", f"{avg_temp:.2f} °C")
        with col2:
            max_precip = filtered_df['PRECTOTCORR'].max()
            st.metric("Max Daily Rainfall", f"{max_precip:.2f} mm")
            
    else:
        st.warning("No data matches the selected filters.")

except Exception as e:
    st.error(f"Error loading data: {e}")
    st.info("Make sure your cleaned CSV files are in the 'data/' folder.")