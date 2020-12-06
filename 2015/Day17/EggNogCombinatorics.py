# Day 17
# How many ways can 150l of eggnog
# be distributed into the containers
# each container has to be filled
# part 2: how many ways can the smallest number of containers be filled

from itertools import combinations

input = open('input.txt')
containers = []
for line in input:
    containers.append(int(line))

total = 0
# worked out these values in my head
max = 13 # for part 2 change this to 5
i = 4
while i < max: 
    for comb in combinations(containers,i):
        if sum(list(comb)) == 150:
            total += 1
    i+=1
print total

