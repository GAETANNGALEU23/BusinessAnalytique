import pandas as pd
df = pd.read_csv('data_dashboard_large.csv')

import streamlit as st 
#import plotly.express as px

# Titre de l'application
st.title("Dashboard Interactif des Ventes")

# Section Résumé 
st.header("Vue d'ensemble")
total_ventes = df['Montant'].sum() 
total_transactions = df.shape[0] 
montant_moyen = df['Montant'].mean() 
satisfaction_moyenne = df['Satisfaction_Client'].mean()

st.metric("Total des ventes (€)", f"{total_ventes:,.2f}")
st.metric("Nombre total de transactions", total_transactions)
st.metric("Montant moyen par transaction (€)", f"{montant_moyen:,.2f}")
st.metric("Satisfaction client moyenne", f"{satisfaction_moyenne:.2f}")
