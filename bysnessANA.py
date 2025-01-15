#import pandas as pd
#df = pd.read_csv('data_dashboard_large.csv')

#import streamlit as st 
#import plotly.express as px

# Titre de l'application
#st.title("Dashboard Interactif des Ventes")

# Section Résumé 
#st.header("Vue d'ensemble")
#total_ventes = df['Montant'].sum() 
#total_transactions = df.shape[0] 
#montant_moyen = df['Montant'].mean() 
#satisfaction_moyenne = df['Satisfaction_Client'].mean()

#st.metric("Total des ventes (€)", f"{total_ventes:,.2f}")
#st.metric("Nombre total de transactions", total_transactions)
#st.metric("Montant moyen par transaction (€)", f"{montant_moyen:,.2f}")
#st.metric("Satisfaction client moyenne", f"{satisfaction_moyenne:.2f}")

# Histogramme des ventes quotidiennes
#df['Date_Transaction'] = pd.to_datetime(df['Date_Transaction'])
#ventes_journalieres = df.groupby(df['Date_Transaction'].dt.date)['Montant'].sum().reset_index()
#fig_ventes_journalieres = px.line(ventes_journalieres, x='Date_Transaction', y='Montant', title='Ventes quotidiennes')
#st.plotly_chart(fig_ventes_journalieres)

# Ajoutez des sections et des graphiques pour les autres analyses 
#st.sidebar.header("Filtres") 
#magasin_filter = st.sidebar.multiselect("Sélectionnez le(s) magasin(s)", options=df['Magasin'].unique())
#if magasin_filter: 
  #df = df[df['Magasin'].isin(magasin_filter)]






import streamlit as st
import pandas as pd
import altair as alt

# Charger les données
data = pd.read_csv('data_dashboard_large - data_dashboard_large.csv')

# Titre du dashboard
st.title("Dashboard Interactif des Performances de l'Entreprise")

# Section Résumé
st.header("Performances")
total_ventes = data['Montant'].sum()
total_transactions = data['ID_Client'].count()
montant_moyen = data['Montant'].mean()
satisfaction_moyenne = data['Satisfaction_Client'].mean()

st.metric("Total des ventes (€)", f"{total_ventes:,.2f}")
st.metric("Nombre total de transactions", total_transactions)
st.metric("Montant moyen par transaction (€)", f"{montant_moyen:,.2f}")
st.metric("Satisfaction client moyenne", f"{satisfaction_moyenne:.2f}")

# Graphique des ventes quotidiennes
st.subheader("Ventes quotidiennes")
data['Date_Transaction'] = pd.to_datetime(data['Date_Transaction'])
ventes_quotidiennes = data.groupby(data['Date_Transaction'].dt.date)['Montant'].sum().reset_index()
chart_ventes_quotidiennes = alt.Chart(ventes_quotidiennes).mark_line().encode(
    x='Date_Transaction:T',
    y='Montant:Q'
).properties(
    title='Ventes quotidiennes'
)
st.altair_chart(chart_ventes_quotidiennes, use_container_width=True)

# Analyse par magasin
st.header("Analyse par magasin")
ventes_par_magasin = data.groupby('Magasin')['Montant'].sum().reset_index()
chart_ventes_par_magasin = alt.Chart(ventes_par_magasin).mark_bar().encode(
    x='Magasin:N',
    y='Montant:Q'
).properties(
    title='Ventes par magasin'
)
st.altair_chart(chart_ventes_par_magasin, use_container_width=True)

transactions_par_magasin = data.groupby('Magasin')['ID_Client'].count().reset_index()
chart_transactions_par_magasin = alt.Chart(transactions_par_magasin).mark_bar().encode(
    x='Magasin:N',
    y='ID_Client:Q'
).properties(
    title='Transactions par magasin'
)
st.altair_chart(chart_transactions_par_magasin, use_container_width=True)

# Analyse des catégories de produits
st.header("Analyse des catégories de produits")
quantites_par_categorie = data.groupby('Categorie_Produit')['Quantite'].sum().reset_index()
chart_quantites_par_categorie = alt.Chart(quantites_par_categorie).mark_bar().encode(
    x='Categorie_Produit:N',
    y='Quantite:Q'
).properties(
    title='Quantités vendues par catégorie'
)
st.altair_chart(chart_quantites_par_categorie, use_container_width=True)

ventes_par_categorie_magasin = data.groupby(['Categorie_Produit', 'Magasin'])['Montant'].sum().reset_index()
chart_ventes_par_categorie_magasin = alt.Chart(ventes_par_categorie_magasin).mark_bar().encode(
    x='Categorie_Produit:N',
    y='Montant:Q',
    color='Magasin:N'
).properties(
    title='Ventes par catégorie et magasin'
)
st.altair_chart(chart_ventes_par_categorie_magasin, use_container_width=True)

# Analyse des modes de paiement
st.header("Analyse des modes de paiement")
transactions_par_mode = data['Mode_Paiement'].value_counts().reset_index()
transactions_par_mode.columns = ['Mode_Paiement', 'Nombre']
chart_transactions_par_mode = alt.Chart(transactions_par_mode).mark_arc().encode(
    theta='Nombre:Q',
    color='Mode_Paiement:N'
).properties(
    title='Répartition des transactions par mode de paiement'
)
st.altair_chart(chart_transactions_par_mode, use_container_width=True)

mode_paiement_populaire = transactions_par_mode.iloc[0]['Mode_Paiement']
st.metric("Mode de paiement le plus utilisé", mode_paiement_populaire)

# Analyse de la satisfaction client
st.header("Analyse de la satisfaction client")
satisfaction_par_magasin = data.groupby('Magasin')['Satisfaction_Client'].mean().reset_index()
chart_satisfaction_par_magasin = alt.Chart(satisfaction_par_magasin).mark_bar().encode(
    x='Magasin:N',
    y='Satisfaction_Client:Q'
).properties(
    title='Satisfaction par magasin'
)
st.altair_chart(chart_satisfaction_par_magasin, use_container_width=True)
