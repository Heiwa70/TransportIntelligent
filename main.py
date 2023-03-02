# This is a sample Python script.
import itertools
import math

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
tabville = [[1, 1], [2, 2], [1, 3], [3, 2], [3, 5], [7, 2]]

def dist_villes(v1,v2):
    return math.sqrt((v2[0] - v1[0])**2 + (v2[1] - v1[1])**2)

def minimal_distance(points):
    paths = list(itertools.permutations(points))
    min_distance = float('inf')
    for path in paths:
        distance_total = 0
        for i in range(len(path)-1):
            distance_total += dist_villes(path[i], path[i+1])
        if distance_total < min_distance:
            min_distance = distance_total
    return min_distance

if __name__ == '__main__':
    min_dist = minimal_distance(tabville)
    print(min_dist)