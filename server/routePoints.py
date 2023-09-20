import requests

# Replace with your Bing Maps API key
api_key = 'Akg2tJWLm6UJu1jjM-aF_OGgQDkJC3xbDV6xgimSckEaBw-ShyHZrWE1MQm0J6o8'

def get_route_coordinates(origin, destination, num_points):
    print("Origin:", origin)
    print("Destination:", destination)
    url = 'https://dev.virtualearth.net/REST/v1/Routes'

    params = {
        'waypoint.1': origin,
        'waypoint.2': destination,
        'key': api_key,
        'routeAttributes': 'routePath',
        'optimize': 'time',
        'maxSolutions': 5  # Number of alternate routes to consider
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        routes = data['resourceSets'][0]['resources']

        # Extract coordinates for num_points on each route
        route_coordinates = {}

        for i, route in enumerate(routes):
            route_coordinates[i] = []
            route_path = route['routePath']['line']['coordinates']

            # Calculate the step size to get num_points
            step = len(route_path) // (num_points - 1)
            for j in range(0, len(route_path), step):
                latitude, longitude = route_path[j]
                route_coordinates[i].append((latitude, longitude))
                if len(route_coordinates[i]) == num_points:
                    break

        return route_coordinates
    else:
        print('Error:', response.status_code)
        return None

# Example coordinates for point A and point B
origin = '49.269802, -123.083763'  # Point A
destination = '49.249896, -122.966601'  # Point B

# Get coordinates for 10 points on each of the 3 routes
# num_points = 10
# route_coordinates = get_route_coordinates(origin, destination, num_points)

# print(route_coordinates)
