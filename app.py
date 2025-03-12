import streamlit as st
import datetime
import requests
import pandas as pd

'''
# TaxiFareModel front
'''
url = 'https://taxifare.lewagon.ai/predict'

with st.form("my_form"):

    pickup_date = st.date_input(
        "When's your ride?",
        value='2014-03-12'
    )
    pickup_time = st.time_input('Set pickup time:', step=300)

    pickup_longitude = st.number_input(
        'Pickup longitude',
        placeholder='Pickup longitude',
        format="%0.6f",
        step=0.000001,
        value=-73.950655
    )
    pickup_latitude = st.number_input(
        'Pickup latitude',
        placeholder='Pickup latitude',
        format="%0.6f",
        step=0.000001,
        value=40.783282
    )
    dropoff_longitude = st.number_input(
        'Dropoff longitude',
        placeholder='Dropoff longitude',
        format="%0.6f",
        step=0.000001,
        value=-73.984365
    )
    dropoff_latitude = st.number_input(
        'Dropoff latitude',
        placeholder='Dropoff latitude',
        format="%0.6f",
        step=0.000001,
        value=40.769802
    )
    passengers = st.slider('Passengers',
        min_value=1,
        max_value=4,
        value=2,
        step=1,
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        params = dict(
            pickup_datetime=datetime.datetime.combine(pickup_date, pickup_time).strftime('%Y-%m-%d %H:%M:%S'),
            pickup_longitude=pickup_longitude,
            pickup_latitude=pickup_latitude,
            dropoff_longitude=dropoff_longitude,
            dropoff_latitude=dropoff_latitude,
            passenger_count=passengers
        )

if submitted:
    endpoint_url = url + f"?{''.join('{}={}&'.format(key, val) for key, val in params.items())}"
    response = requests.get(endpoint_url)
    f'''
    '''
    st.markdown("### Submitted parameters:")
    st.write(params)
    st.markdown(f"### Predicted price: `${round(response.json()['fare'], 2)}`")
    df = pd.DataFrame([
        {"color": '#65d2d9',"latitude": params["pickup_latitude"], "longitude": params["pickup_longitude"]},
        {"color": '#5fd76a',"latitude": params["dropoff_latitude"], "longitude": params["dropoff_longitude"]}
    ])
    st.map(df, color='color')
else:
    df = pd.DataFrame([
        {"color": '#65d2d9', "latitude": pickup_latitude, "longitude": pickup_longitude},
        {"color": '#5fd76a', "latitude": dropoff_latitude, "longitude": dropoff_longitude}
    ])
    st.map(df, color='color')
