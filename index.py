python
import requests
import pandas as pd
import json

# Define API endpoint for the real-time public transportation dataset
API_ENDPOINT = "https://api.abudhabi-transport.ae/v1/ridership"

# Define parameters for fetching data (adjust as needed)
params = {
    "start_date": "2023-01-01",
    "end_date": "2023-01-31",
    "format": "json"
}

# Fetch data from the API
response = requests.get(API_ENDPOINT, params=params)
if response.status_code == 200:
    data = response.json()
else:
    print(f"Failed to fetch data. HTTP status code: {response.status_code}")

# Convert JSON data to a Pandas DataFrame
data_df = pd.DataFrame(data['ridership'])

# Save the data to a CSV file
data_df.to_csv('public_transportation_ridership.csv', index=False)

print("Data fetched and saved to public_transportation_ridership.csv")
