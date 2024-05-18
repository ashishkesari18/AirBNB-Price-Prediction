import streamlit as st
import pickle
import pandas as pd
import requests
from sklearn.preprocessing import LabelEncoder
import math
import time

# Load dataset
merged_df = pd.read_csv("Airbnb_Data.csv")

# Load the pre-trained model
with open(r'xgboost.pkl', 'rb') as file:
    model = pickle.load(file)

# Initialize LabelEncoder for 'room_type'
label_encoder = LabelEncoder()
merged_df['room_type'] = label_encoder.fit_transform(merged_df['room_type'])

def get_lat_long(city):
    # Geocode city name to latitude and longitude using OpenStreetMap API
    url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        data = response.json()
        if data:
            latitude = float(data[0]['lat'])
            longitude = float(data[0]['lon'])
            return latitude, longitude
        else:
            return None, None
    except requests.exceptions.RequestException as e:
        print("Error fetching data from OpenStreetMap API:", e)
        return None, None
    finally:
        # Add a delay of 1 second between requests
        time.sleep(1)


def transform_input_values(room_type, no_of_bathrooms, amenities, accommodates, zipcode, city):
    latitude, longitude = get_lat_long(city)

    if latitude is None or longitude is None:
        return None, "Error: City not found or invalid"
    else:
        input_values = {
            'room_type': label_encoder.transform([room_type])[0],
            'bathrooms': float(no_of_bathrooms),
            'amenities': int(amenities),
            'accommodates': int(accommodates),
            'zipcode': int(zipcode),
            'latitude': latitude,
            'longitude': longitude
        }
        return input_values, None

def predict_result(input_values):
    if input_values is None:
        return "Error: One or more inputs are invalid"
    print("Input values being used for prediction:", input_values)  # Debug statement
    
    # Prepare input data as DataFrame
    input_df = pd.DataFrame([input_values])
    
    # Reorder columns to match expected feature order
    input_df = input_df[['room_type', 'bathrooms', 'amenities', 'accommodates', 'zipcode', 'latitude', 'longitude']]

    # Rename columns to match expected feature names
    input_df.columns = ['room_type', 'bathrooms', 'longitude', 'latitude', 'zipcode', 'accommodates', 'amenities']

    prediction = model.predict(input_df)
    return prediction[0]

def main():
    st.title('Air-BnB Price Prediction')
    st.header('Enter Input Values:')

    room_type_options = label_encoder.inverse_transform(merged_df['room_type'].unique())
    room_type = st.selectbox('Room Type', room_type_options)
    no_of_bathrooms = st.text_input('No of Bathrooms', '')
    amenities = st.text_input('Amenities', '')  
    accommodates = st.text_input('Accommodates', '')
    zipcode = st.text_input('zipcode', '')
    city = st.text_input('City Name', '')

    if st.button('Submit'):
        input_values, error_message = transform_input_values(room_type, no_of_bathrooms, amenities, accommodates, zipcode, city)
        if input_values:
            prediction = predict_result(input_values)
            prediction = round(math.exp(prediction), 2)
            st.success(f'Predicted Price: {prediction} USD')
        else:
            st.error(error_message)

if __name__ == '__main__':
    main()


