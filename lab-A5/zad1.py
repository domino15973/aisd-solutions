from random import shuffle
from math import sqrt

path = "TSP.txt"

cities = []
with open(path) as txt:
    for line in txt:
        cities.append(line.split())

shuffle(cities)

start = [0, 0, 0]  # start position
distance = 0

# random path
for city in cities:
    distance += sqrt((float(city[1]) - float(start[1])) ** 2 + (float(city[2]) - float(start[2])) ** 2)
    start = city

# back to start position
distance += sqrt((float(cities[0][1]) - float(start[1])) ** 2 + (float(cities[0][2]) - float(start[2])) ** 2)

print("Path: ", end="")
for city in cities:
    print(city[0], end="->")
print(cities[0][0])

print("First city: " + cities[0][0])
print("Total distance: " + str(distance))
