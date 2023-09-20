import routePoints as rp
from distanceFinder import calculate_distance_matrix

hotspots = [
    (49.273878, -123.044158),
    (49.258080, -123.033771),
    (49.345, -122.9983)
]

origin = '49.269802, -123.083763'  # Point A
destination = '49.249896, -122.966601'  # Point B

def calculate_distance(origin, destination):
    return ((destination[1] - origin[1]) ** 2 + (destination[0] - origin[0]) ** 2) ** 0.5

def find_min(list1):
    return min(list1)


def safestRoute(origin, destination, hotspots):
    route_coordinates = rp.get_route_coordinates(origin, destination, 10)

    list_min_distances = []

    for hotspot in hotspots:
        listroutemin = []
        for i in route_coordinates:
            listdistances = [calculate_distance(hotspot, coord) for coord in route_coordinates[i]]
            min_distance = find_min(listdistances)
            origin_str = ','.join(map(str, route_coordinates[i][listdistances.index(min_distance)]))
            dest_str = ','.join(map(str, hotspot))
            listroutemin.append(calculate_distance_matrix([origin_str], [dest_str]))
        list_min_distances.append(listroutemin)

    list_sums = [sum(route) for route in zip(*list_min_distances)]
    # print(list_sums)

    return list_sums.index(min(list_sums))
