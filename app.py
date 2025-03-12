import streamlit as st
import datetime
import requests
import pandas as pd

'''
# TaxiFareModel front
'''
url = 'https://taxifarededev-768760105976.europe-west1.run.app/predict'

'''pickup_datetime=2014-07-06%2019:18:00&pickup_longitude=-73.950655&pickup_latitude=40.783282&dropoff_longitude=-73.984365&dropoff_latitude=40.769802&passenger_count=2'''
with st.form("my_form"):

    pickup_date = st.date_input(
        "When's your ride?"
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
    passengers = st.number_input(
        'Number of passengers',
        placeholder='Number of passengers',
        step=1,
        value=2
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        params = dict(
            pickup_datetime=datetime.datetime.combine(pickup_date, pickup_time).strftime('%Y/%m/%d %H:%M:%S'),
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
    Submitted parameters:
    '''
    st.write(params)
    f'''
    Predicted price: **${round(response.json()['fare'], 2)}**
    '''
    df = pd.DataFrame([
        {"latitude": params["pickup_latitude"], "longitude": params["pickup_longitude"]},
        {"latitude": params["dropoff_latitude"], "longitude": params["dropoff_longitude"]}
    ])
    st.write(df)
    st.map(df)
else:
    st.map()
