import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('driver_avgPos_circuit.csv')

df.loc[df['driverRef']=='max_verstappen', 'pilot'] = 'verstappen'

fig, axes = plt.subplots(figsize=(15,5))
for pil in df.driverRef.unique():
    d = df.loc[df['driverRef']==pil]
    plt.plot(d.location, d.media, label=pil)
    plt.scatter(d.location, d.media, s=2*d.somma**2, linewidths=1, edgecolors='xkcd:steel grey')
axes.invert_yaxis()
axes.set_facecolor('k')
axes.xaxis.grid()
fig.set_facecolor('xkcd:steel grey')
axes.grid(linewidth=.3)
plt.legend(loc='lower center')


st.write('### Ordinativi e consegne')

st.pyplot(fig)
