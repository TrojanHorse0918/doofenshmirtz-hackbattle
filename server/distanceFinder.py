import requests

# Replace with your Bing Maps API key
api_key = 'Akg2tJWLm6UJu1jjM-aF_OGgQDkJC3xbDV6xgimSckEaBw-ShyHZrWE1MQm0J6o8'

def calculate_distance_matrix(origin_coords, destination_coords):
    # print(origin_coords, destination_coords)
    url = 'https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix'
    
    params = {
        'origins': ';'.join(origin_coords),
        'destinations': ';'.join(destination_coords),
        'travelMode': 'driving',
        'key': api_key
    }

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        distances = data['resourceSets'][0]['resources'][0]['results']
        distanceMatrix = [distance['travelDistance'] for distance in distances]
        if distanceMatrix:
            return distanceMatrix[0]
    else:
        print('Error:', response.status_code)
        return None

# Example coordinates
origin_coords = ['49.269802, -123.083763']  # Latitude and longitude for point 1
destination_coords = ['49.249896, -122.966601']    # Latitude and longitude for point 2

# distance = calculate_distance_matrix(origin_coords, destination_coords)
# print(distance, "kilometres")