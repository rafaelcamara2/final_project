
import streamlit as st
import pandas as pd
import plotly_express as px

@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

car_data = load_data('vehicles_us.csv')

st.header('Vehicle Ads Dashboard')

hist_button = st.button('Create Histogram')
scatter_button = st.button('Create Scatter Plot')

if hist_button:
    st.write('Creating a histogram for column "odometer"')
    fig_h = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_h, use_container_width=True, key="hist_btn")

if scatter_button:
    st.write('Creating a scatter plot for "odometer" vs "price"')
    fig_s = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_s, use_container_width=True, key="scat_btn")

st.subheader('Optional: Use checkboxes')
build_histogram = st.checkbox('Create Histogram (checkbox)')
build_scatter = st.checkbox('Create Scatter Plot (checkbox)')

if build_histogram:
    st.write('Creating a histogram for column "odometer" (checkbox)')
    fig_h2 = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_h2, use_container_width=True, key="hist_cb")

if build_scatter:
    st.write('Creating a scatter plot for "odometer" vs "price" (checkbox)')
    fig_s2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_s2, use_container_width=True, key="scat_cb")
