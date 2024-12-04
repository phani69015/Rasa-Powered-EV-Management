from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import numpy as np
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import pandas as pd
import joblib
import requests
from textwrap import dedent  
from actions.env import API

class ActionBatterySoc(Action):
    def name(self) -> str:
        return "action_battery_soc"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Fetch SoC value (replace with actual data fetching)
        soc = 85  # Example value
        return [SlotSet("battery_soc", soc)]
    

class ActionBatterySoh(Action):
    def name(self) -> str:
        return "action_battery_soh"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Fetch SoH value (replace with actual data fetching)
        soh = 95  # Example value
        return [SlotSet("battery_soh", soh)]


class ActionBatteryTemperature(Action):
    def name(self) -> str:
        return "action_battery_temperature"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Fetch temperature value (replace with actual data fetching)
        temperature = 32  # Example value in °C
        return [SlotSet("battery_temperature", temperature)]

class ActionChargingStatus(Action):
    def name(self) -> str:
        return "action_charging_status"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Fetch charging status (replace with actual data fetching)
        charging_status = "Charging at 3.6 kW."  # Example value
        return [SlotSet("charging_status", charging_status)]


class ActionEnergyConsumption(Action):
    def name(self) -> str:
        return "action_energy_consumption"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Fetch energy consumption (replace with actual data fetching)
        energy_consumption = 150  # Example value in Wh/km
        return [SlotSet("energy_consumption", energy_consumption)]


class ActionEstimatedRange(Action):
    def name(self) -> str:
        return "action_estimated_range"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Fetch estimated range (replace with actual data fetching)
        estimated_range = 250  # Example value in km
        return [SlotSet("estimated_range", estimated_range)]

class ActionBatteryVoltage(Action):
    def name(self) -> str:
        return "action_battery_voltage"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Fetch battery voltage (replace with actual data fetching)
        voltage = 400  # Example value in volts
        return [SlotSet("battery_voltage", voltage)]


class ActionBatteryCurrent(Action):
    def name(self) -> str:
        return "action_battery_current"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Fetch battery current (replace with actual data fetching)
        current = 100  # Example value in amps
        return [SlotSet("battery_current", current)]


class ActionChargingPower(Action):
    def name(self) -> str:
        return "action_charging_power"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Fetch charging power (replace with actual data fetching)
        charging_power = 3.6  # Example value in kW
        return [SlotSet("charging_power", charging_power)]


class ActionBatteryCapacity(Action):
    def name(self) -> str:
        return "action_battery_capacity"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Fetch battery capacity (replace with actual data fetching)
        capacity = 75  # Example value in kWh
        return [SlotSet("battery_capacity", capacity)]


class ActionBatteryCycleCount(Action):
    def name(self) -> str:
        return "action_battery_cycle_count"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Fetch cycle count (replace with actual data fetching)
        cycle_count = 250  # Example value
        return [SlotSet("battery_cycle_count", cycle_count)]


class ActionBatteryFaults(Action):
    def name(self) -> str:
        return "action_battery_faults"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Fetch battery faults (replace with actual data fetching)
        faults = "No faults detected."  # Example value
        return [SlotSet("battery_faults", faults)]


class ActionRegenerativeBraking(Action):
    def name(self) -> str:
        return "action_regenerative_braking"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Fetch regenerative braking data (replace with actual data fetching)
        regenerative_braking = "Recovering 10% energy during braking."  # Example value
        return [SlotSet("regenerative_braking", regenerative_braking)]


class ActionChargeDischargeRate(Action):
    def name(self) -> str:
        return "action_c_rate"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Fetch C-rate (replace with actual data fetching)
        c_rate = 1.0  # Example value
        return [SlotSet("c_rate", c_rate)]


class ActionChargingStationInfo(Action):
    def name(self) -> str:
        return "action_charging_station_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Fetch charging station information (replace with actual data fetching)
        station_info = "Connected to a fast charger at 123 Main St."  # Example value
        return [SlotSet("charging_station_info", station_info)]


class ActionBatteryCoolingStatus(Action):
    def name(self) -> str:
        return "action_battery_cooling_status"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Fetch cooling system status (replace with actual data fetching)
        cooling_status = "Cooling system is functioning normally."  # Example value
        return [SlotSet("battery_cooling_status", cooling_status)]


class ActionRemainingChargeTime(Action):
    def name(self) -> str:
        return "action_remaining_charge_time"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Fetch remaining charge time (replace with actual data fetching)
        remaining_time = "45 minutes to full charge."  # Example value
        return [SlotSet("remaining_charge_time", remaining_time)]


class ActionDrivingModeImpact(Action):
    def name(self) -> str:
        return "action_driving_mode_impact"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Fetch driving mode impact data (replace with actual data fetching)
        impact = "Eco mode extends range by 10%."  # Example value
        return [SlotSet("driving_mode_impact", impact)]


class ActionBatteryAging(Action):
    def name(self) -> str:
        return "action_battery_aging"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Fetch battery aging indicator (replace with actual data fetching)
        aging_status = "Battery aging is normal."  # Example value
        return [SlotSet("battery_aging", aging_status)]

class ActionChargingHistory(Action):
    def name(self) -> str:
        return "action_charging_history"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Fetch charging history (replace with actual data fetching)
        history = "Last charged at 10:00 AM for 2 hours."  # Example value
        return [SlotSet("charging_history", history)]


class ActionPreconditioningStatus(Action):
    def name(self) -> str:
        return "action_preconditioning_status"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Fetch preconditioning status (replace with actual data fetching)
        preconditioning = "Battery is being preconditioned for charging."  # Example value
        return [SlotSet("preconditioning_status", preconditioning)]


class ActionBatteryImbalance(Action):
    def name(self) -> str:
        return "action_battery_imbalance"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Fetch battery imbalance data (replace with actual data fetching)
        imbalance = "Battery cells are balanced."  # Example value
        return [SlotSet("battery_imbalance", imbalance)]

class ActionSafetySystemsStatus(Action):
    def name(self) -> str:
        return "action_safety_systems_status"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Fetch safety systems status (replace with actual data fetching)
        safety_status = "All safety systems are operational."  # Example value
        return [SlotSet("safety_systems_status", safety_status)]

class ActionEnvironmentalConditions(Action):
    def name(self) -> str:
        return "action_environmental_conditions"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Fetch environmental conditions (replace with actual data fetching)
        conditions = "Temperature: 25°C, Humidity: 60%."  # Example value
        return [SlotSet("environmental_conditions", conditions)]


class ActionAuxiliaryPowerUsage(Action):
    def name(self) -> str:
        return "action_auxiliary_power_usage"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Fetch auxiliary power usage (replace with actual data fetching)
        auxiliary_usage = 1.5  # Example value in kW
        
        # Set the slot with auxiliary usage data
        return [SlotSet("auxiliary_power_usage", auxiliary_usage)]

class ActionAuxiliaryPowerUsage(Action):
    def name(self) -> str:
        return "action_auxiliary_power_usage"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Fetch auxiliary power usage (replace with actual data fetching)
        auxiliary_usage = 1.5  # Example value in kW
        
        # Set the slot with auxiliary usage data
        return [SlotSet("auxiliary_power_usage", auxiliary_usage)]



import pandas as pd
from geopy.distance import geodesic
import numpy as np
import math
import pyproj
from geographiclib.geodesic import Geodesic

class EVTripPlanner:
    # Constants for Nissan Leaf 2016 model
    battery_capacity = 60  # kWh
    energy_consumed_per_km = 0.2  # kWh/km (Energy consumption per km)
    charger_efficiency = 0.95  # 95%

    def __init__(self, stations_file):
        self.df = pd.read_csv(stations_file)
        self.df['lattitude'] = pd.to_numeric(self.df['lattitude'], errors='coerce')
        self.df['longitude'] = pd.to_numeric(self.df['longitude'], errors='coerce')
        self.df['lattitude'].fillna(self.df['lattitude'].median(), inplace=True)
        self.df['longitude'].fillna(self.df['longitude'].median(), inplace=True)

    # Function to calculate distance between two lat/long points
    def calculate_distance(self, lat1, lon1, lat2, lon2):
        R = 6371.0
        dlat = np.radians(lat2 - lat1)
        dlon = np.radians(lon2 - lon1)
        a = np.sin(dlat / 2)**2 + np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * np.sin(dlon / 2)**2
        c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
        distance = R * c
        return distance

    # Function to calculate SOC after driving a certain distance
    def calculate_soc(self, d_j, C_bat, EC):
        soc_j = (1 - (EC * d_j) / C_bat) * 100  
        return soc_j

    # Function to calculate energy required to charge from current SOC to full SOC
    def calculate_energy_required(self, soc_j, soc_f, C_bat, eta):
        E_req_j = ((soc_f - soc_j) / 100) * C_bat / eta  # Energy needed in kWh
        return E_req_j

    def calculate_bearing(self, lat1, lat2, long1, long2):
        brng = Geodesic.WGS84.Inverse(lat1, long1, lat2, long2)['azi1']
        return brng

    # Function to find the closest station within range and in the correct direction
    def find_closest_station(self, current_lat, current_lon, dest_lat, dest_lon, min_range, max_range, tolerance_angle=20):
        stations_in_range = []
        dest_bearing = self.calculate_bearing(current_lat, current_lon, dest_lat, dest_lon)

        for _, station in self.df.iterrows():
            distance_to_station = self.calculate_distance(current_lat, current_lon, station['lattitude'], station['longitude'])
            distance_to_dest_from_station = self.calculate_distance(station['lattitude'], station['longitude'], dest_lat, dest_lon)
            distance_to_dest_from_current = self.calculate_distance(current_lat, current_lon, dest_lat, dest_lon)

            if min_range <= distance_to_station <= max_range:
                station_bearing = self.calculate_bearing(current_lat, current_lon, station['lattitude'], station['longitude'])

                # Ensure the station's bearing is close to the destination bearing within a balanced tolerance
                bearing_difference = abs(dest_bearing - station_bearing)
                if (bearing_difference <= tolerance_angle or bearing_difference >= (360 - tolerance_angle)) and distance_to_dest_from_station <= distance_to_dest_from_current:
                    stations_in_range.append((f"{station['name']} ({station['city']})", station['lattitude'], station['longitude'], station['ac_fast_price'], station['dc_fast_price'], distance_to_station))

        # Sort by distance and return the closest station
        stations_in_range.sort(key=lambda x: x[5])

        if stations_in_range:
            return stations_in_range[0]  # Return the closest station in direction
        else:
            return None

    # Function to plan stops and calculate charging cost
    def plan_stops(self, total_distance, current_soc, min_soc, max_range, dest_lat, dest_lon):
        remaining_distance = total_distance
        stops = []
        current_lat, current_lon = 16.5812639, 80.5263493  # Starting location
        soc = current_soc  # current state of charge in percentage
        total_cost1 = total_cost2 = 0

        while remaining_distance > 0:
            # Calculate distance that can be traveled with the current SOC
            available_range = (soc / 100) * max_range

            if remaining_distance <= available_range - (min_soc / 100) * max_range:
                print(f"Car can cover the remaining distance of {remaining_distance:.2f} km without charging again.")
                break

            next_distance = available_range - (min_soc / 100) * max_range
            print(next_distance)
            # Find the next station within the range and in the direction of the destination
            min_range = available_range * 0.5  # Start looking at 50% of available range
            station = self.find_closest_station(current_lat, current_lon, dest_lat, dest_lon, min_range, available_range)

            if station:
                stops.append(station[0])
                current_lat, current_lon = station[1], station[2]

                # Calculate how much charge is left after driving to this station
                soc = self.calculate_soc(next_distance, self.battery_capacity, self.energy_consumed_per_km)

                # Calculate energy required to charge from current SOC to 100%
                energy_needed = self.calculate_energy_required(soc, 100, self.battery_capacity, self.charger_efficiency)
                charge_cost1 = energy_needed * station[3]  # Assuming AC charge cost
                charge_cost2 = energy_needed * station[4]  # Assuming DC charge cost
                total_cost1 += charge_cost1
                total_cost2 += charge_cost2

                soc = 100
                remaining_distance -= next_distance
                print('Remaining distance:', remaining_distance)
            else:
                break  # No station found, trip not feasible

        return stops, total_cost1, total_cost2, remaining_distance
    def get_lat_long(self, api_key, address):
            headers = {
                "X-Authorization-Token": api_key
            }

            url = f"https://apihub.latlong.ai/v4/geocode.json?address={address}"
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                location_data = response.json()

                if 'data' in location_data:
                    data = location_data['data']
                    latitude = float(data['latitude'])
                    longitude = float(data['longitude'])
                    return latitude, longitude
                else:
                    print("Error: 'data' field missing in the response.")
                    return None
            else:
                print(f"Error: Unable to fetch data (status code: {response.status_code})")
                return None
    def trip_summary(self,stops, total_cost1, total_cost2, remaining_distance,total_distance):
        summary = "Trip Plan Summary:(current location: Vijayawada)"
        summary+=f"total distance is {total_distance}\n "

        if stops:
            summary += "Charging Stops :"
            for i, stop in enumerate(stops, 1):
                # Ensure that latitude and longitude are treated as floats
                summary += f"  Stop {i}: {stop} "
        else:
            summary += "No charging stops required. The vehicle can cover the entire distance with the current charge."

        summary += f"\nTotal Charging Cost for AC Fast Charging: Rs {total_cost1:.2f} and "
        summary += f"Total Charging Cost for DC Fast Charging: Rs {total_cost2:.2f} "

        summary += f" and Car can cover the remaining distance of {remaining_distance:.2f} km without charging again."

        return summary
# actions.py

master = pd.read_csv("C://4-1//Rasa//charging_stations_with_prices.csv")

class ActionPlanTrip(Action):

    def name(self):
        return "action_plan_trip"


    def run(self, dispatcher, tracker, domain):
        destination = tracker.get_slot("destination")
        if destination:
            destination=str(destination)
            # Instantiate the class
            # Sample input data
            api=API()
            api_key = api
            # Fetch user's and destination's latitude and longitude
            user_latitude, user_longitude =   16.5812639, 80.5263493
            
            master="C://4-1//Rasa//charging_stations_with_prices.csv"
            trip_planner = EVTripPlanner(master)
            dest_latitude, dest_longitude = trip_planner.get_lat_long(api_key, destination)
            current_soc = 0   
            min_soc = 10   
                        
            total_distance = trip_planner.calculate_distance(user_latitude, user_longitude, dest_latitude, dest_longitude)
            total_distance=total_distance*1.25# Total trip distance
            max_range = trip_planner.battery_capacity / trip_planner.energy_consumed_per_km  # Max range based on battery and energy consumption

            # Calculate stops and cost
            stops, total_cost1, total_cost2, remaining_distance = trip_planner.plan_stops(total_distance, current_soc, min_soc, max_range, dest_latitude, dest_longitude)


            # Example usage:
            recommendation_message = trip_planner.trip_summary(stops, total_cost1, total_cost2, remaining_distance,total_distance)
            print(recommendation_message)
        # Get recommendations
            if recommendation_message:
                return [SlotSet("trip_cost", recommendation_message)]
            else:
                dispatcher.utter_message(text=f"Sorry, I couldn't find the location '{destination}'. Please provide a valid destination.")
        else:
            dispatcher.utter_message(text="Please provide a destination.")
        
        return []
