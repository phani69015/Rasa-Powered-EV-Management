# import pandas as pd
# import numpy as np
# import joblib
# import requests
# from textwrap import dedent

# # Load the dataset
# master = pd.read_csv("C://4-1//Rasa//charging_stations_with_prices.csv")

# class PlanTrip:
    
#     def haversine(self, lat1, lon1, lat2, lon2):
#         R = 6371.0
#         dlat = np.radians(lat2 - lat1)
#         dlon = np.radians(lon2 - lon1)
#         a = np.sin(dlat / 2)**2 + np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * np.sin(dlon / 2)**2
#         c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
#         distance = R * c
#         return distance
    
#     def calculate_bearing(self, lat1, lon1, lat2, lon2):
#         lat1 = np.radians(lat1)
#         lon1 = np.radians(lon1)
#         lat2 = np.radians(lat2)
#         lon2 = np.radians(lon2)

#         delta_lon = lon2 - lon1
#         x = np.sin(delta_lon) * np.cos(lat2)
#         y = np.cos(lat1) * np.sin(lat2) - (np.sin(lat1) * np.cos(lat2) * np.cos(delta_lon))

#         initial_bearing = np.arctan2(x, y)
#         compass_bearing = (np.degrees(initial_bearing) + 360) % 360

#         return compass_bearing
    
#     def add_distances_energies(self, df, latu, longu, latd, longd, ev_efficiency_kwh_per_km):
#         df['distance_from_user'] = df.apply(lambda row: self.haversine(latu, longu, row['lattitude'], row['longitude']), axis=1)
#         df['distance_to_destination'] = df.apply(lambda row: self.haversine(row['lattitude'], row['longitude'], latd, longd), axis=1)
#         df['energy_needed_user_to_station'] = df['distance_from_user'] * ev_efficiency_kwh_per_km
        
#         # Load pre-trained model
#         loaded_model = joblib.load('C://4-1//Rasa//actions//model.joblib')
#         df['total_energy_needed_kWh'] = loaded_model.predict(df[['distance_from_user', 'distance_to_destination', 'ac_slow_price', 'ac_fast_price', 'dc_slow_price', 'dc_fast_price']])
#         return df 
    
#     def get_lat_long(self, api_key, address):
#         headers = {
#             "X-Authorization-Token": api_key
#         }

#         url = f"https://apihub.latlong.ai/v4/geocode.json?address={address}"
#         response = requests.get(url, headers=headers)

#         if response.status_code == 200:
#             location_data = response.json()

#             if 'data' in location_data:
#                 data = location_data['data']
#                 latitude = float(data['latitude'])
#                 longitude = float(data['longitude'])
#                 return latitude, longitude
#             else:
#                 print("Error: 'data' field missing in the response.")
#                 return None
#         else:
#             print(f"Error: Unable to fetch data (status code: {response.status_code})")
#             return None
        
#     def get_recommendations(self, dest, user_latitude, user_longitude, dest_latitude, dest_longitude, battery_status, df):
#         df['ac_slow_cost'] = df['total_energy_needed_kWh'] * df['ac_slow_price']
#         df['ac_fast_cost'] = df['total_energy_needed_kWh'] * df['ac_fast_price']
#         df['dc_slow_cost'] = df['total_energy_needed_kWh'] * df['dc_slow_price']
#         df['dc_fast_cost'] = df['total_energy_needed_kWh'] * df['dc_fast_price']
#         reachable_stations = df.loc[df['energy_needed_user_to_station'] <= battery_status]
#         bearing_to_dest = self.calculate_bearing(user_latitude, user_longitude, dest_latitude, dest_longitude)
        
#         reachable_stations['bearing_to_station'] = reachable_stations.apply(
#             lambda row: self.calculate_bearing(user_latitude, user_longitude, row['lattitude'], row['longitude']), axis=1)

#         direction_threshold = 30
#         reachable_stations_in_direction = reachable_stations.loc[
#             (reachable_stations['bearing_to_station'] >= bearing_to_dest - direction_threshold) &
#             (reachable_stations['bearing_to_station'] <= bearing_to_dest + direction_threshold)
#         ]
        
#         if not reachable_stations_in_direction.empty:
#             best_ac_slow = reachable_stations_in_direction.loc[reachable_stations_in_direction['ac_slow_cost'].idxmin()]
#             best_dc_fast = reachable_stations_in_direction.loc[reachable_stations_in_direction['dc_fast_cost'].idxmax()]
#             best_ac_fast = reachable_stations_in_direction.loc[reachable_stations_in_direction['ac_fast_cost'].idxmax()]
#             best_dc_slow = reachable_stations_in_direction.loc[reachable_stations_in_direction['dc_slow_cost'].idxmin()]
#         else:
#             return "No reachable charging stations found in the direction of your trip."

#         recommendation_paragraph = dedent(f"""
#                 Based on your current battery status and direction towards {dest}, here are the best charging stations:
                
#                 For a more economical AC slow charge, consider stopping at {best_ac_slow['name']} in {best_ac_slow['city']}. 
#                 The AC slow charging will cost approximately ₹{best_ac_slow['ac_slow_cost']:.2f}.
                
#                 For a faster AC charge, you can stop at {best_ac_fast['name']} in {best_ac_fast['city']}. 
#                 The AC fast charging will cost approximately ₹{best_ac_fast['ac_fast_cost']:.2f}.
                
#                 For a more economical DC slow charge, {best_dc_slow['name']} in {best_dc_slow['city']} is an ideal stop. 
#                 The DC slow charging will cost approximately ₹{best_dc_slow['dc_slow_cost']:.2f}.
                
#                 For a faster DC charge, consider {best_dc_fast['name']} in {best_dc_fast['city']}. 
#                 The DC fast charging will cost approximately ₹{best_dc_fast['dc_fast_cost']:.2f}.
#                 """)
        
#         return recommendation_paragraph

# # Instantiate the class
# trip_planner = PlanTrip()

# # Sample input data
# destination = 'Delhi'
# curr_location = 'Vijayawada'
# battery_status = 50  # 50% battery
# ev_efficiency_kwh_per_km = 0.15
# api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJUb2tlbklEIjoiM2NjZjE0N2MtZGVhMy00ZjM3LTk2MDAtNTY0N2NhOTNmMGVkIiwiQ2xpZW50SUQiOiI5Y2RjYzg3Yy1kZjhiLTQ2NTYtYTMwYy03Y2UwMTYyYjA4ZWEiLCJCdW5pdElEIjoxMDczOCwiQXBwTmFtZSI6IlRpcnVtYWxhICh0aXJ1bWFsYXBoYW5lbmRyYUBnbWFpbC5jb20pIC0gU2lnbiBVcCIsIkFwcElEIjoxMTc4NCwiVGltZVN0YW1wIjoiMjAyNC0xMC0wMiAxMjoxNzowOSIsImV4cCI6MTczMDQ2MzQyOX0.tlb-ebXhPcTIaFlMzT3zATiOQJvkuOCSbnwkIMlTndo"  # Replace with your API key

# # Fetch user's and destination's latitude and longitude
# user_latitude, user_longitude = trip_planner.get_lat_long(api_key, curr_location)
# dest_latitude, dest_longitude = trip_planner.get_lat_long(api_key, destination)
# df=master.copy()
# df['lattitude'] = pd.to_numeric(df['lattitude'], errors='coerce')
# df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
# df['lattitude'].fillna(df['lattitude'].median(), inplace=True)
# df['longitude'].fillna(df['longitude'].median(), inplace=True)
# # Add distances and energy requirements to the dataset
# data = trip_planner.add_distances_energies(df, user_latitude, user_longitude, dest_latitude, dest_longitude, ev_efficiency_kwh_per_km)

# # Get recommendations
# recommendation_message = trip_planner.get_recommendations(destination, user_latitude, user_longitude, dest_latitude, dest_longitude, battery_status, data)

# # Output the recommendations
# print(recommendation_message)
import pandas as pd
import numpy as np
import joblib
from textwrap import dedent



class PlanTrip:
    
    def haversine(self, lat1, lon1, lat2, lon2):
        R = 6371.0
        dlat = np.radians(lat2 - lat1)
        dlon = np.radians(lon2 - lon1)
        a = np.sin(dlat / 2)**2 + np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * np.sin(dlon / 2)**2
        c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
        distance = R * c
        return distance
    
    def calculate_bearing(self, lat1, lon1, lat2, lon2):
        lat1 = np.radians(lat1)
        lon1 = np.radians(lon1)
        lat2 = np.radians(lat2)
        lon2 = np.radians(lon2)

        delta_lon = lon2 - lon1
        x = np.sin(delta_lon) * np.cos(lat2)
        y = np.cos(lat1) * np.sin(lat2) - (np.sin(lat1) * np.cos(lat2) * np.cos(delta_lon))

        initial_bearing = np.arctan2(x, y)
        compass_bearing = (np.degrees(initial_bearing) + 360) % 360

        return compass_bearing
    
    def add_distances_energies(self, df, latu, longu, latd, longd, ev_efficiency_kwh_per_km):
        df['distance_from_user'] = df.apply(lambda row: self.haversine(latu, longu, row['lattitude'], row['longitude']), axis=1)
        df['distance_to_destination'] = df.apply(lambda row: self.haversine(row['lattitude'], row['longitude'], latd, longd), axis=1)
        df['energy_needed_user_to_station'] = df['distance_from_user'] * ev_efficiency_kwh_per_km
        
        # Load pre-trained model
        loaded_model = joblib.load('model.joblib')
        df['total_energy_needed_kWh'] = loaded_model.predict(df[['distance_from_user', 'distance_to_destination', 'ac_slow_price', 'ac_fast_price', 'dc_slow_price', 'dc_fast_price']])
        return df 
    
    def get_multiple_charging_stations(self, user_latitude, user_longitude, dest_latitude, dest_longitude, battery_status, max_range, ev_efficiency_kwh_per_km, df):
        stops = []
        current_latitude = user_latitude
        current_longitude = user_longitude
        remaining_distance_to_dest = self.haversine(user_latitude, user_longitude, dest_latitude, dest_longitude)
        
        while remaining_distance_to_dest > max_range:
            # Add distance from current position to all stations
            df['distance_from_current_position'] = df.apply(
                lambda row: self.haversine(current_latitude, current_longitude, row['lattitude'], row['longitude']), axis=1)
            
            # Filter stations within current range
            reachable_stations = df[df['distance_from_current_position'] <= max_range]
            
            if reachable_stations.empty:
                return "No charging stations found within range. You cannot reach the destination with the current setup."
            
            # Find the best station (can be based on price or proximity)
            best_station = reachable_stations.loc[reachable_stations['distance_from_current_position'].idxmin()]
            
            stops.append(best_station)
            
            # Update current position to the best station
            current_latitude = best_station['lattitude']
            current_longitude = best_station['longitude']
            
            # Recalculate remaining distance to destination
            remaining_distance_to_dest = self.haversine(current_latitude, current_longitude, dest_latitude, dest_longitude)
            
            # Assume full recharge at each stop
            battery_status = 100
        
        # Add the destination as the final stop
        stops.append({'name': 'Destination', 'city': 'Delhi', 'lattitude': dest_latitude, 'longitude': dest_longitude})
        
        return stops
    
    def get_recommendations(self, dest, user_latitude, user_longitude, dest_latitude, dest_longitude, battery_status, df, ev_efficiency_kwh_per_km, battery_capacity_kwh, max_range):
        df['soc_j'] = (1 - (ev_efficiency_kwh_per_km * df['distance_from_user']) / battery_capacity_kwh) * 100
        
        # Get multiple stops for the trip
        stops = self.get_multiple_charging_stations(user_latitude, user_longitude, dest_latitude, dest_longitude, battery_status, max_range, ev_efficiency_kwh_per_km, df)
        
        if isinstance(stops, str):
            return stops  # If no stops found, return the error message
        
        # Generate the recommendation message
        recommendation_paragraph = "Your trip from Vijayawada to Delhi requires the following charging stops:\n\n"
        for i, stop in enumerate(stops[:-1]):  # Exclude destination in loop
            recommendation_paragraph += dedent(f"""
            Stop {i+1}: {stop['name']} in {stop['city']}
            Distance from current position: {stop['distance_from_current_position']:.2f} km
            Estimated cost for charging (AC slow): ₹{stop['ac_slow_price']:.2f}
            """)
        
        recommendation_paragraph += "\nYou will reach your destination in Delhi after the final stop.\n"
        return recommendation_paragraph

# Instantiate the class
trip_planner = PlanTrip()

# Sample input data
destination = 'Delhi'
user_latitude = 16.5062  
user_longitude = 80.6480  # Vijayawada coordinates
dest_latitude = 28.6139   # Delhi coordinates
dest_longitude = 77.2090
battery_status = 50  # Percentage
ev_efficiency_kwh_per_km = 0.2  # Example efficiency (kWh/km)
battery_capacity_kwh = 40  # Example battery capacity (kWh)
max_range = 130  # Max range of EV in km with full battery
master = pd.read_csv("C://4-1//Rasa//charging_stations_with_prices.csv")
# Load dataset
df = master.copy()
df['lattitude'] = pd.to_numeric(df['lattitude'], errors='coerce')
df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
df['lattitude'].fillna(df['lattitude'].median(), inplace=True)
df['longitude'].fillna(df['longitude'].median(), inplace=True)
# Add distances and energy consumption to the dataframe
df = trip_planner.add_distances_energies(df, user_latitude, user_longitude, dest_latitude, dest_longitude, ev_efficiency_kwh_per_km)

# Get the trip recommendations
recommendation = trip_planner.get_recommendations(destination, user_latitude, user_longitude, dest_latitude, dest_longitude, battery_status, df, ev_efficiency_kwh_per_km, battery_capacity_kwh, max_range)

# Print the recommendations
print(recommendation)
