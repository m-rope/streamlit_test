from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials
import streamlit as st

db = firestore.Client.from_service_account_json("formula1_firebase_key.json")

# Create a reference to the Google post.
doc_ref = db.collection("gestionale").document("ORD01")

# Then get the data at that reference.
doc = doc_ref.get()

# Let's see what we got!
st.write("The id is: ", doc.id)
st.write("The contents are: ", doc.to_dict())
