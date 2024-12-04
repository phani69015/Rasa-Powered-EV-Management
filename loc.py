import requests
api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJUb2tlbklEIjoiZmI4NWNhNzUtZGI4NS00NTVhLTg2MzctZTk0ZjA2ODhmYWViIiwiQ2xpZW50SUQiOiJkNGNjMjY2MC02YzUxLTQxZmEtYTdmNC01ZDI2MTQ2YmMzYWYiLCJCdW5pdElEIjoxMDc3MSwiQXBwTmFtZSI6IlBoYW5lbmRyYSgyMTAwMDY5MDE1ZWVlQGdtYWlsLmNvbSkgLSBTaWduIFVwIiwiQXBwSUQiOjEyMzQ1LCJUaW1lU3RhbXAiOiIyMDI0LTExLTA4IDAzOjU2OjEzIiwiZXhwIjoxNzMzNjMwMTczfQ.BekYxU1R9fllHGU_5XTNOEapgeAYHsXQX2oHyBc6oLw"  # Replace with your API key

# def get_lat_long( api_key, address):
#     headers = {
#         "X-Authorization-Token": api_key
#     }

#     url = f"https://apihub.latlong.ai/v4/geocode.json?address={address}"
#     response = requests.get(url, headers=headers)

#     if response.status_code == 200:
#         location_data = response.json()

#         if 'data' in location_data:
#             data = location_data['data']
#             latitude = float(data['latitude'])
#             longitude = float(data['longitude'])
#             return latitude, longitude
#         else:
#             print("Error: 'data' field missing in the response.")
#             return None
#     else:
#         print(f"Error: Unable to fetch data (status code: {response.status_code})")
#         return None

# print(get_lat_long(api_key,'srikakulam'))


import requests

url = "https://apihub.latlong.ai/v4/geocode.json?address=srikakulam&accuracy_level=true"

payload={}
headers = {
        "X-Authorization-Token": api_key
    }
response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
