a = {"type": "service_account", "project_id": "formula1-f8b52", "private_key_id": "6643c452afda982ee7a2f815e8198bf64d80dcf9", "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC+7Y5V3oPfdJeq\nUEX30ESC0zAkQoBaphM1YgFVXjc3/g5KtvnW5h4/juZo+UJhNxLNol87v9uVEyFv\nWuade8a5I43FxmGlXXwGd38GZ8Gai4m14kVtGHKX/KKCzn0AWqWYoSbVF7+cZdld\nYgzyDPyTCEzexCkg/a6A3XilGrIIt4RhFqkbAHVY4Igt2ivssO6xPG5r8FCxDClm\nPqH3Wy01AMEGBtFs5w0z4lfpvG4IdAfoBW4SQdIhV7UZxshMtSu4kWKIuW3lBiW3\ne3poVXLn/h6vuWcc64xbCdU0/gxeqO9AU5JIjsoALeboAt+exF41fC9Hk3QvEzAX\nBHoeRXK/AgMBAAECggEAFliKsnrNkmdR95QCQbkgG55eDGW1d2aSlEqOf2WnLtLO\n7L2yS2LkIr+LMLljpH8j9en4HW/HYmY6do78CMMw2gBS79UtHoPs0nuajq8GwMYY\nwwSNkvGBOqVN2+NmS+v6ulIPenHsx4BAICbWqbRivKQEYy+Fj3VBaZcCL3NgEkGR\nvphZRe0f0BUxdIKhjKwnCKG2OkGPiV/V37MVCSEQf35Mdd+SfcgY1BcH9KtLqSnd\nsR7B9dAt1c4qtKS/SlBtiSMpR91OJZMQx7R4/ttEOR0eY6HoraYB1F8hYz1YVQhV\nVXpH+TS6nkiIatU31JOuASnNZzPzWomYlfk+cJRKIQKBgQDvdzXvSbmFb/TgTmyr\n0eeHp1tCMk+F7E3buMbKfzAWCYsdpaJIsAp22j5xuoWB/85Y5iFQnztIM0M8QEm1\nHifu+rudXOeJ3p1s7zcLt1mL5OcCEOrsdzJ05KyV7gQOPuE9rNJhJsixQdc2tjYt\nd3DBesPUtf8zNWOyEZ9buQ1tLwKBgQDMHGTUcRwGcUIzysbSa5wIcBVX1i04XTvo\np6PZr/fzHe1S3pVzQSRS7Pxl3cJaabfvAri5cujeZHN8WWPYaryioPQHFixQtdV6\n7y+G9JJJ/Zr2A2xbOPlyEyyPgqZB0ajXtVDLMtD4xP9duRT/hkYIA5txZbCasbgF\nZ+QtDZWPcQKBgQDI0m+v4mMsbayuI/bszVbfI9HbnPel93uABeDo12tLP+ukDFEh\npkjQTczKccMfN5kkYrKTu0XrEdqT/9IQi16wAyQuH0iqDcB2J9NBBx2YvXmh+PAb\nKQdukovOHNLX45HfuDyibvUl+nJzFrIuxRkRmVP74jlIB8E5B6BeOr3wzwKBgCiJ\nmxz2OfKtm9BdfY9c/+hNGnAPgXuoSLW0Vb5uTHhkgTXsLxJs5aHyn0479NWwGW/G\nwplSUR2aJbWUq1fYGw7RmKWvqa1976Ay0OWkvUkkrRofI+4aKrCVTkxSTmLUGQx+\nXkV9GjPOLEmY8KqvKEl/LegfoiuXEE1CjPbFs+aBAoGBAMC+VdrepRufCbKE9NRU\nnALsBwFcMMBd5bzeXX8hOUP4fijk8odYXQh5MI3xKEOfnBvcGMcY4nVuxongFZnw\nfnoqppC8rQSoSy/uTiYGz6rwNxIknT6SzT2jW7uqzwjmF9dodqd/SvtZvsbdNXP6\nuASNlSSkqXCwqZZ9Q3Jaob60\n-----END PRIVATE KEY-----\n", "client_email": "firebase-adminsdk-40agk@formula1-f8b52.iam.gserviceaccount.com", "client_id": "112176980452451105591", "auth_uri": "https://accounts.google.com/o/oauth2/auth", "token_uri": "https://oauth2.googleapis.com/token", "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs", "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-40agk%40formula1-f8b52.iam.gserviceaccount.com",}

import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd

if not firebase_admin._apps:
    cred = credentials.Certificate(a)
    firebase_admin.initialize_app(cred)

db = firestore.client()

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
