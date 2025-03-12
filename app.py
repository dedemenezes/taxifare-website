import streamlit as st
import datetime
import requests

'''
# TaxiFareModel front
'''
url = 'https://taxifarededev-768760105976.europe-west1.run.app/predict'


st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

with st.form("my_form"):

    pickup_date = st.date_input(
        "When's your ride?"
    )
    pickup_time = st.time_input('Set pickup time:', step=300)

    pickup_longitude = st.number_input(
        'Pickup longitude',
        placeholder='Pickup longitude',
        format="%0.8f"
    )
    pickup_latitude = st.number_input(
        'Pickup latitude',
        placeholder='Pickup latitude',
        format="%0.8f"
    )
    dropoff_longitude = st.number_input(
        'Dropoff longitude',
        placeholder='Dropoff longitude',
        format="%0.8f"
    )
    dropoff_latitude = st.number_input(
        'Dropoff latitude',
        placeholder='Dropoff latitude',
        format="%0.8f"
    )
    passengers = st.number_input(
        'Number of passengers',
        placeholder='Number of passengers',
        format="%0.0f"
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        params = dict(
            pickup_datetime=datetime.datetime.combine(pickup_date, pickup_time).strftime('%Y/%m/%d %H:%M:%S'),
            pickup_longitude=pickup_longitude,
            pickup_latitude=pickup_latitude,
            dropoff_longitude=dropoff_longitude,
            dropoff_latitude=dropoff_latitude,
            passenger_count=int(passengers)
        )
        st.write(params)


'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

# url = 'https://taxifarededev-768760105976.europe-west1.run.app/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...
'''


'''
3. Let's call our API using the `requests` package...
'''
# endpoint_url = url + f"?{''.join('{}={}&'.format(key, val) for key, val in params.items())}"
# st.page_link(endpoint_url, label='endpoint')
# response = requests.get(endpoint_url)
# st.write(response)
'''
4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

if submitted:
    endpoint_url = url + f"?{''.join('{}={}&'.format(key, val) for key, val in params.items())}"
    # st.page_link(endpoint_url, label='endpoint')
    response = requests.get(endpoint_url)
    # st.write(response.json())
    f'''
    Predicted price: ${round(response.json()['fare'], 2)}
    '''
