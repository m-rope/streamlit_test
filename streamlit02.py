from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials
import streamlit as st
import pandas as pd


db = firestore.Client.from_service_account_json("formula1_firebase_key.json")

res = db.collection('gestionale').stream()
dati=[{'ordine':x.id,**x.to_dict()} for x in res]

df=pd.DataFrame(dati)[['ordine','id','origine','importo','consegna']]
df.set_index('ordine',inplace=True)

st.write('### Ordinativi e consegne')
st.bar_chart(df.groupby('origine')['importo'].sum())
zona = st.sidebar.radio(
    "Zona:",
    ('Tutte', 'EUR', 'NAM'))
standard = st.sidebar.checkbox('Solo consegna normale')

if standard:
    df=df[df.consegna=='STANDARD']
if zona == 'EUR':
    st.dataframe(df[df.origine=='EUR'])
elif zona == 'NAM':
    st.dataframe(df[df.origine=='NAM'])
else:
    st.dataframe(df)
