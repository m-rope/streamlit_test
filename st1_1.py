from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials
'''
#cred = credentials.Certificate("formula1_firebase_key.json")
cred = "formula1_firebase_key.json"
db = firestore.Client.from_service_account_json(cred)
# Add a new user to the database
doc_ref = db.collection('users').document('alovelace')
doc_ref.set({
    'first': 'Ada',
    'last': 'Lovelace',
    'born': 1815
})

# Then query to list all users
users_ref = db.collection('users')

for doc in users_ref.stream():
    print('{} => {}'.format(doc.id, doc.to_dict()))
'''
import streamlit as st

st.header('Hello 🌎!')
if st.button('Balloons?'):
    st.balloons()
