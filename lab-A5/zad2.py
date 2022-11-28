from math import inf, sqrt
import numpy as np

path = "TSP.txt"

cities = []
with open(path) as txt:
    for line in txt:
        cities.append(line.split())

n_cities = len(cities)

adj_matrix = np.array(np.zeros([n_cities, n_cities]))
for x in range(n_cities):
    for y in range(n_cities):
        adj_matrix[x][y] = sqrt((float(cities[x][1]) - float(cities[y][1])) ** 2 + (float(cities[x][2]) - float(cities[y][2])) ** 2)

# greedy algorithm
path = [0]
length = 0
for i in range(n_cities - 1):
    min = inf
    for j in range(n_cities):
        if (j not in path and adj_matrix[path[-1]][j] < min):
            min = adj_matrix[path[-1]][j]
            min_j = j

    length += min
    path.append(min_j)

length += adj_matrix[path[-1]][0]
path.append(0)

print("Path: " + str(path))
print("Length: " + str(length))
