import distanceFinder as df
import routePoints as rp

#note: INEFFICIENT CODE


hotspots = [
    (49.273878, -123.044158),
    (49.258080, -123.033771),
    (49.345, -122.9983)
]

def calculateDistance(origin, destination):
    # origin = origin.split(", ")
    dist = (((float(destination[1]) - float(origin[1]))**2) + ((float(destination[0]) - float(origin[0]))**2))**(0.5)
    return dist

def findMin(list1):
    min = list1[0]
    for i in list1:
        if i<min:
            min = i
    return list1.index(min)

origin = '49.269802, -123.083763'  # Point A
destination = '49.249896, -122.966601'  # Point B

route_coordinates = rp.get_route_coordinates(origin, destination, 10)

# print(route_coordinates)

list_min_distances = []

for num in range(len(hotspots)):
    listroutemin = []
    for i in route_coordinates:
        listdistances = []
        for coord in route_coordinates[i]:
            listdistances.append(calculateDistance(hotspots[num], coord))
        minIndex = findMin(listdistances)
        origin = str(route_coordinates[i][minIndex][0]) + ',' + str(route_coordinates[i][minIndex][1])
        dest = str(hotspots[num][0]) + ',' + str(hotspots[num][1])
        listroutemin.append(df.calculate_distance_matrix([origin], [dest]))
        # print("Hotspot", num+1, "Route", i+1, ":", listdistances)
    list_min_distances.append(listroutemin)


list_sums = []

for i in range(len(route_coordinates)):
    sum = 0
    for j in range(len(hotspots)):
        sum+=list_min_distances[j][i]
    list_sums.append(sum)

print(list_sums)
    

