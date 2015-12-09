# Day 9
# Travelling salesman problem
# Only 8 houses so using brute force
# using permutations tool from itertools
from itertools import permutations

def total_distance(paths,order):
    dist = 0
    for i in range(len(order)-1):
        dist += paths[order[i],order[i+1]]
    return dist

if __name__ == '__main__':
    input = open('input.txt')
    paths = {}
    houses = []
    for line in input:
        words = line.split(' ')
        paths[words[0],words[2]] = int(words[4])
        paths[words[2],words[0]] = int(words[4])
        if words[0] not in houses:
            houses.append(words[0])
        if words[2] not in houses:
            houses.append(words[2])
    input.close()

    shortestPath = 10000000
    longestPath = 0
    for perm in permutations(houses):
        dist = total_distance(paths,list(perm))
        if dist < shortestPath:
            shortestPath = dist
            print 'shortest path so far: {}'.format(list(perm))
        if dist > longestPath:
            longestPath = dist
            print 'longest path so far: {}'.format(list(perm))
    print shortestPath,longestPath
