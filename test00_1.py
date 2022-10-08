import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('driver_avgPos_circuit.csv')

df.loc[df['driverRef']=='max_verstappen', 'pilot'] = 'verstappen'

fig1, axes = plt.subplots(figsize=(15,5))
for pil in df.pilot.unique():
    d = df.loc[df['pilot']==pil]
    plt.plot(d.location, d.media, label=pil)
    plt.scatter(d.location, d.media, s=2*d.somma**2, linewidths=1, edgecolors='xkcd:steel grey')
axes.invert_yaxis()
axes.set_facecolor('k')
axes.xaxis.grid()
fig1.set_facecolor('xkcd:steel grey')
axes.grid(linewidth=.3)
plt.legend(loc='lower center')

fig2, axes = plt.subplots(figsize=(15,5))
for pil in df.pilot.unique():
    d = df.loc[df['pilot']==pil]
    plt.plot(d.location, d.somma, label=pil)
    plt.scatter(d.location, d.somma, s=3000/d.media, linewidths=1, edgecolors='xkcd:steel grey')
axes.invert_yaxis()
axes.set_facecolor('k')
axes.xaxis.grid()
fig2.set_facecolor('xkcd:steel grey')
axes.grid(linewidth=.3)
plt.legend(loc='center')


st.write('### Ordinativi e consegne')


metrica = st.sidebar.radio(
    "Metrica:",
    ('Totale partecipazioni GP', 'Media posizione di arrivo'))
#standard = st.sidebar.checkbox('Solo consegna normale')

#if standard:
#    df=df[df.consegna=='STANDARD']
if metrica == 'Totale partecipazioni GP':
    st.pyplot(fig1)
else:
    st.pyplot(fig2)