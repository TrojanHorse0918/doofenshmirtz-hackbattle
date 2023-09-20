import requests
from requests.structures import CaseInsensitiveDict
import json
import cityfinder as cf

places_api_key = 'e9a274a7128248eaa947fdec39674c86'

def get_chemists(start_long, start_lat, end_long, end_lat):
    print("Start city: ", cf.get_city_from_lat_lng(start_lat, start_long))
    print("End city: ", cf.get_city_from_lat_lng(end_lat, end_long))

    url = "https://api.geoapify.com/v2/places?categories=commercial.chemist&filter=circle%3A{}%2C{}%2C{}&limit=20&apiKey=e9a274a7128248eaa947fdec39674c86"

    url = url.format(start_long, start_lat, 5000)

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    resp = requests.get(url, headers=headers)
    data = resp.json()

    # print(data)
    for feature in data['features']:
        def print_if_exists(key, value):
            if value is not None:
                print(f"{key}: {value}")

        # Print each field only if it exists in the dictionary
        print_if_exists("Name", feature['properties'].get('name'))
        print_if_exists("Country", feature['properties'].get('country'))
        print_if_exists("State", feature['properties'].get('state'))
        print_if_exists("County", feature['properties'].get('county'))
        print_if_exists("City", feature['properties'].get('city'))
        print_if_exists("Post Code", feature['properties'].get('postcode'))
        print_if_exists("Street", feature['properties'].get('street'))
        print_if_exists("Latitude", feature['properties'].get('lat'))
        print_if_exists("Longitude", feature['properties'].get('lon'))
        print_if_exists("Address Line 1", feature['properties'].get('address_line1'))
        print_if_exists("Address Line 2", feature['properties'].get('address_line2'))
        print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

    print(resp.status_code)

print("CHEMISTS")
get_chemists(-123.083763, 49.269802, -122.966601, 49.249896)
print('========================================================================================================================================================================================')
print('========================================================================================================================================================================================')


def get_hospitals(start_long, start_lat, end_long, end_lat):
    print("Start city: ", cf.get_city_from_lat_lng(start_lat, start_long))
    print("End city: ", cf.get_city_from_lat_lng(end_lat, end_long))

    url = "https://api.geoapify.com/v2/places?categories=healthcare.hospital&filter=circle%3A{}%2C{}%2C{}&limit=20&apiKey=e9a274a7128248eaa947fdec39674c86"

    url = url.format(start_long, start_lat, 5000)

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    resp = requests.get(url, headers=headers)
    data = resp.json()

    # print(data)
    for feature in data['features']:
        def print_if_exists(key, value):
            if value is not None:
                print(f"{key}: {value}")

        # Print each field only if it exists in the dictionary
        print_if_exists("Name", feature['properties'].get('name'))
        print_if_exists("Country", feature['properties'].get('country'))
        print_if_exists("State", feature['properties'].get('state'))
        print_if_exists("County", feature['properties'].get('county'))
        print_if_exists("City", feature['properties'].get('city'))
        print_if_exists("Post Code", feature['properties'].get('postcode'))
        print_if_exists("Street", feature['properties'].get('street'))
        print_if_exists("Latitude", feature['properties'].get('lat'))
        print_if_exists("Longitude", feature['properties'].get('lon'))
        print_if_exists("Address Line 1", feature['properties'].get('address_line1'))
        print_if_exists("Address Line 2", feature['properties'].get('address_line2'))
        print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

    print(resp.status_code)

print("HOSPITALS")
get_hospitals(-123.083763, 49.269802, -122.966601, 49.249896)
print('========================================================================================================================================================================================')
print('========================================================================================================================================================================================')

def get_policeStations(start_long, start_lat, end_long, end_lat):
    print("Start city: ", cf.get_city_from_lat_lng(start_lat, start_long))
    print("End city: ", cf.get_city_from_lat_lng(end_lat, end_long))

    url = "https://api.geoapify.com/v2/places?categories=service.police&filter=circle%3A{}%2C{}%2C{}&limit=20&apiKey=e9a274a7128248eaa947fdec39674c86"

    url = url.format(start_long, start_lat, 5000)

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    resp = requests.get(url, headers=headers)
    data = resp.json()

    # print(data)
    for feature in data['features']:
        def print_if_exists(key, value):
            if value is not None:
                print(f"{key}: {value}")

        # Print each field only if it exists in the dictionary
        print_if_exists("Name", feature['properties'].get('name'))
        print_if_exists("Country", feature['properties'].get('country'))
        print_if_exists("State", feature['properties'].get('state'))
        print_if_exists("County", feature['properties'].get('county'))
        print_if_exists("City", feature['properties'].get('city'))
        print_if_exists("Post Code", feature['properties'].get('postcode'))
        print_if_exists("Street", feature['properties'].get('street'))
        print_if_exists("Latitude", feature['properties'].get('lat'))
        print_if_exists("Longitude", feature['properties'].get('lon'))
        print_if_exists("Address Line 1", feature['properties'].get('address_line1'))
        print_if_exists("Address Line 2", feature['properties'].get('address_line2'))
        print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

    print(resp.status_code)

print("POLICE STATIONS")
get_policeStations(-123.083763, 49.269802, -122.966601, 49.249896)
print('========================================================================================================================================================================================')
print('========================================================================================================================================================================================')


def get_childcare(start_long, start_lat, end_long, end_lat):
    print("Start city: ", cf.get_city_from_lat_lng(start_lat, start_long))
    print("End city: ", cf.get_city_from_lat_lng(end_lat, end_long))

    url = "https://api.geoapify.com/v2/places?categories=childcare.kindergarten&filter=circle%3A{}%2C{}%2C{}&limit=20&apiKey=e9a274a7128248eaa947fdec39674c86"

    url = url.format(start_long, start_lat, 5000)

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    resp = requests.get(url, headers=headers)
    data = resp.json()

    # print(data)
    for feature in data['features']:
        def print_if_exists(key, value):
            if value is not None:
                print(f"{key}: {value}")

        # Print each field only if it exists in the dictionary
        print_if_exists("Name", feature['properties'].get('name'))
        print_if_exists("Country", feature['properties'].get('country'))
        print_if_exists("State", feature['properties'].get('state'))
        print_if_exists("County", feature['properties'].get('county'))
        print_if_exists("City", feature['properties'].get('city'))
        print_if_exists("Post Code", feature['properties'].get('postcode'))
        print_if_exists("Street", feature['properties'].get('street'))
        print_if_exists("Latitude", feature['properties'].get('lat'))
        print_if_exists("Longitude", feature['properties'].get('lon'))
        print_if_exists("Address Line 1", feature['properties'].get('address_line1'))
        print_if_exists("Address Line 2", feature['properties'].get('address_line2'))
        print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

    print(resp.status_code)

print("CHILDCARE")
get_childcare(-123.083763, 49.269802, -122.966601, 49.249896)
print('========================================================================================================================================================================================')
print('========================================================================================================================================================================================')