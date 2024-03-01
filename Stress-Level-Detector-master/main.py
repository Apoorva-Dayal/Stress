"""This is the main module to run the app"""

# Importing the necessary Python modules.
import streamlit as st #streamlit is an open-source app framework that lets you create web apps from data scripts in pure Python, without front-end experience.

# Import necessary functions from web_functions
from web_functions import load_data

# Import pages
from Tabs import home, data, predict, visualise

# Configure the app
st.set_page_config(
    page_title = 'Stress Level Detector',
    page_icon = 'heavy_exclamation_mark',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)

# Dictionary for pages
Tabs = {
    "Home": home,
    "Data Info": data,
    "Prediction": predict,
    "Visualisation": visualise
    
}

# Create a sidebar
# Add title to sidear
st.sidebar.title("Navigation")

# Create radio option to select the page
page = st.sidebar.radio("Pages", list(Tabs.keys()))

# Loading the dataset.
df, X, y = load_data()

# Call the app funciton of selected page to run
if page in ["Prediction", "Visualisation"]:
    Tabs[page].app(df, X, y)
elif (page == "Data Info"):
    Tabs[page].app(df)
else:
    Tabs[page].app()