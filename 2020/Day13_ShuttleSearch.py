# Part 1:
# given a starting point and a list of multipliers, find the next multiple from that start point.
# return the distance * multiple
# Part 2:
# What is the earliest timestamp such that all of the listed bus IDs depart at offsets matching their positions in the list? x counts as 1.
from math import lcm
from functools import reduce

file = open('input_13.txt', 'r')
start = int(file.readline().strip('\n'))
buses = file.readline().strip('\n').split(',')
file.close()

buses_part1 = [int(x) for x in buses if x.isdigit()]
next_stop_time = [x - start % x for x in buses_part1]
part1 = buses_part1[next_stop_time.index(min(next_stop_time))]*min(next_stop_time)

bus_times = {}
for i, v in enumerate(buses):
    if v.isdigit():
        bus_times[int(v)] = i

i = 2
buses_part1 = sorted(buses_part1, reverse=True)
lcm_var = lcm(buses_part1[0], buses_part1[1])
max_bus=1
while True:
    if max_bus > 1:
        t+=lcm_var
    else:
        t = i*buses_part1[0] - bus_times[buses_part1[0]]
    check = True
    for b in buses_part1[max_bus:]:
        if (t+bus_times[b]) % b != 0:
            check = False
            break
        print(i, b, t, max_bus)
        max_bus+=1
        lcm_var = reduce(lambda x,y: lcm(x,y), buses_part1[0:max_bus])
    if check == True:
        part2 = t
        break
    if max_bus == 1:
        i+=1

print('Part 1: {}, Part 2: {}'.format(part1, part2))
