import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
user_latitude=16.24346322150367
user_longitude=80.64468120987304
dest_latitude=28.644079712431942
dest_longitude=77.1149803419578
master = pd.read_csv("C://4-1//Rasa//charging_stations_with_prices.csv")
df=master.copy() 

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0
    dlat = np.radians(lat2 - lat1)
    dlon = np.radians(lon2 - lon1)
    a = np.sin(dlat / 2)**2 + np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * np.sin(dlon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    distance = R * c
    return distance

ev_efficiency_kwh_per_km = 0.15
# Ensure that latitude and longitude are numerical
df['lattitude'] = pd.to_numeric(df['lattitude'], errors='coerce')
df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
df['lattitude'].fillna(df['lattitude'].median(), inplace=True)
df['longitude'].fillna(df['longitude'].median(), inplace=True)
# Calculate distances from user to each station and to the destination
df['distance_from_user'] = df.apply(lambda row: haversine(user_latitude, user_longitude, row['lattitude'], row['longitude']), axis=1)
df['distance_to_destination'] = df.apply(lambda row: haversine(row['lattitude'], row['longitude'], dest_latitude, dest_longitude), axis=1)

# Calculate the energy needed for each leg (from user to station and from station to destination)
df['energy_needed_user_to_station'] = df['distance_from_user'] * ev_efficiency_kwh_per_km
df['energy_needed_station_to_destination'] = df['distance_to_destination'] * ev_efficiency_kwh_per_km

# Total energy needed
df['total_energy_needed_kWh'] = df['energy_needed_user_to_station'] + df['energy_needed_station_to_destination']


# Train a machine learning model to predict energy consumption
X = df[['distance_from_user', 'distance_to_destination', 'ac_slow_price', 'ac_fast_price', 'dc_slow_price', 'dc_fast_price']]
y = df['total_energy_needed_kWh']  # Target: energy needed


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Random Forest model for regression
model = RandomForestRegressor()
model.fit(X_train, y_train)

import joblib

joblib.dump(model, 'model.joblib')
