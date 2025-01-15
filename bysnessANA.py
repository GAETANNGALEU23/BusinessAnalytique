import pandas as pd
df = pd.read_csv('data_dashboard_large.csv')

import streamlit as st 
import plotly.express as px

# Titre de l'application
st.title("Dashboard Interactif des Ventes")
