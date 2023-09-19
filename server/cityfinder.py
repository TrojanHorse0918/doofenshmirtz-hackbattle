import requests

def get_city_from_lat_lng(latitude, longitude):
    # Bing Maps API endpoint for reverse geocoding
    api_key = "Akg2tJWLm6UJu1jjM-aF_OGgQDkJC3xbDV6xgimSckEaBw-ShyHZrWE1MQm0J6o8"
    url = f'https://dev.virtualearth.net/REST/v1/Locations/{latitude},{longitude}?o=json&key={api_key}'

    try:
        # Send a GET request to the Bing Maps API
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200 and 'resourceSets' in data and data['resourceSets']:
            resources = data['resourceSets'][0].get('resources', [])
            if resources:
                address = resources[0].get('address', {})
                if 'locality' in address:
                    return address['locality']

        raise ValueError('Could not determine city.')

    except requests.RequestException as e:
        raise ValueError(f'Error fetching data: {e}')

# latitude = 37.7749
# longitude = -122.4194

# try:
#     city = get_city_from_lat_lng(latitude, longitude)
#     print('City:', city)
# except ValueError as e:
#     print('Error:', str(e))

