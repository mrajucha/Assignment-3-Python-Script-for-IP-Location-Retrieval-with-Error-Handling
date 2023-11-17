#Python script to that retrieves IP location information from the API provided

import requests
import json

def my_ip_location():
    # API URL for IP location information
    api_url = "https://ipapi.co/json/"

    try:
        # GET request to the API
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            ip_data = response.json()

            # Extract relevant information
            ip_address = ip_data.get('ip', 'N/A')
            city = ip_data.get('city', 'N/A')
            region = ip_data.get('region', 'N/A')
            country = ip_data.get('country_name', 'N/A')
            timezone = ip_data.get('timezone', 'N/A')

            # Display the information on the console
            print(f"IP Address: {ip_address}")
            print(f"City: {city}")
            print(f"Region: {region}")
            print(f"Country: {country}")
            print(f"Timezone: {timezone}")
        else:
            print(f"Error: Unable to retrieve data. Status Code: {response.status_code}")

    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Call the function to get and display IP location information
    my_ip_location()


# import requests
# import json
# import time

# def get_ip_location():
#     # API URL for IP location information
#     api_url = "https://ipapi.co/json/"

#     try:
#         # Make a GET request to the API
#         response = requests.get(api_url)

#         # Check if the request was successful (status code 200)
#         response.raise_for_status()

#         # Parse the JSON response
#         ip_data = response.json()

#         # Extract relevant information
#         ip_address = ip_data.get('ip', 'N/A')
#         city = ip_data.get('city', 'N/A')
#         region = ip_data.get('region', 'N/A')
#         country = ip_data.get('country_name', 'N/A')
#         timezone = ip_data.get('timezone', 'N/A')

#         # Display the information on the console
#         print(f"IP Address: {ip_address}")
#         print(f"City: {city}")
#         print(f"Region: {region}")
#         print(f"Country: {country}")
#         print(f"Timezone: {timezone}")

#     except requests.RequestException as e:
#         print(f"Error: {e}")
        
#         # Handle rate limit exceeded (429 status code)
#         if response.status_code == 429:
#             # Sleep for a while before retrying
#             retry_after = int(response.headers.get('Retry-After', 10))
#             print(f"Rate limit exceeded. Waiting for {retry_after} seconds before retrying...")
#             time.sleep(retry_after)
#             # Retry the request
#             get_ip_location()

# if __name__ == "__main__":
#     # Call the function to get and display IP location information
#     get_ip_location()
