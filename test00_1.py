import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('driver_avgPos_circuit.csv')

df.loc[df['driverRef']=='max_verstappen', 'pilot'] = 'verstappen'

fig, axes = plt.subplots(figsize=(15,5))
sns.lineplot(data=df, x='location', y='media', hue='driverRef')
sns.scatterplot(data=df, x='location', y='media', hue='driverRef', size='somma', sizes=(50,400), legend=False)
axes.invert_yaxis()
axes.set_facecolor('k')
axes.xaxis.grid()
fig.set_facecolor('xkcd:steel grey')
axes.grid(linewidth=.3)
plt.legend(loc='lower center')


st.write('### Ordinativi e consegne')

st.pyplot(fig)
