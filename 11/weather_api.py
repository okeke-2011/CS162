import requests
import pandas as pd

client_id = '57d66924-38e5-4dfd-993c-66a6201b5b5c'

endpoint = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=60.10&lon=9.58'
# Issue an HTTP GET request
r = requests.get(endpoint, auth=(client_id, ''))
# Extract JSON data
json = r.json()
print(json)