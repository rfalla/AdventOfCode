# Part 1: You have a ship initialized at 0,0 facing East.
# Given directions like:
#    Action N means to move north by the given value.
#    Action S means to move south by the given value.
#    Action E means to move east by the given value.
#    Action W means to move west by the given value.
#    Action L means to turn left the given number of degrees.
#    Action R means to turn right the given number of degrees.
#    Action F means to move forward by the given value in the direction the ship is currently facing.
# What is the manhatten distance at the end of the instructions?
#
# Part 2: The instructions now mean:
#    Action N means to move the waypoint north by the given value.
#    Action S means to move the waypoint south by the given value.
#    Action E means to move the waypoint east by the given value.
#    Action W means to move the waypoint west by the given value.
#    Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
#    Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
#    Action F means to move forward to the waypoint a number of times equal to the given value.
# What is the Manhatten distance this time?
from math import cos, sin, radians
import numpy as np
directions_part1 = {'N': lambda n, r: (0, n, 0)
              , 'S': lambda n, r: (0, -n, 0)
              , 'E': lambda n, r: (n, 0, 0)
              , 'W': lambda n, r: (-n, 0, 0)
              , 'L': lambda n, r: (0, 0, radians(n))
              , 'R': lambda n, r: (0, 0, -radians(n))
              , 'F': lambda n, r: (n*cos(r), n*sin(r), 0)}

directions_part2 = {'N': lambda n, r: (0, 0, 0, n)
                    , 'S': lambda n, r: (0, 0, 0, -n)
                    , 'E': lambda n, r: (0, 0, n, 0)
                    , 'W': lambda n, r: (0, 0, -n, 0)
                    , 'L': lambda n, r: (0, 0, r[0]*cos(radians(n))-r[1]*sin(radians(n))-r[0]
                                         , r[0]*sin(radians(n))+r[1]*cos(radians(n))-r[1])
                    , 'R': lambda n, r: (0, 0, r[0]*cos(radians(n))+r[1]*sin(radians(n))-r[0]
                                         , -r[0]*sin(radians(n))+r[1]*cos(radians(n))-r[1])
                    , 'F': lambda n, r: (n*r[0], n*r[1], 0, 0)}

instructions = [x.strip() for x in open('input_12.txt')]
ship = np.zeros(3) #(EW, NS, direction)
for i in instructions:
    ship += directions_part1[i[0]](int(i[1:]), ship[2])
part1 = abs(ship[0]) + abs(ship[1])

ship = np.zeros(4)#EW_ship, NS_ship, EW_WP, NS_WP)
#The waypoint starts 10 units east and 1 unit north relative to the ship.
ship[2] = 10
ship[3] = 1
for i in instructions:
    ship += directions_part2[i[0]](int(i[1:]), ship[2:])
part2 = abs(ship[0])+abs(ship[1])

print('Part 1: {}, Part 2: {}'.format(part1, part2))
