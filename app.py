import streamlit as st
import requests
'''
# TaxiFareModel front
'''

st.markdown('''
# Paramètres de la course
Ici nous voudrions accéder aux informations de votre course
''')

date_time = st.text_input("Date et heure ?", "2013-07-06 17:18:00")
pickup_longitude = st.text_input("Longitude de départ ?", "-73.950655")
pickup_latitude = st.text_input("Latitude de départ ?", "40.783282")
dropoff_longitude = st.text_input("Longitude d'arrivée ?", "-73.984365")
dropoff_latitude = st.text_input("Latitude d'arrivée ?", "40.769802")
passenger_counter = st.text_input("Nombre de passagers ?","1")


url = 'https://apitaxi-gnqszluqma-ew.a.run.app/predict'

params = {
    "pickup_datetime": date_time,
    "pickup_longitude": float(pickup_longitude),
    "pickup_latitude": float(pickup_latitude),
    "dropoff_longitude": float(dropoff_longitude),
    "dropoff_latitude": float(dropoff_latitude),
    "passenger_count": int(passenger_counter)}


response = requests.get(url, params=params)

st.write('## Et tu te fais donc plumer de :', f'{round(response.json()["prediction"],1)} $')
