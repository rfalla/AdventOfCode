# Day 3
# Directions given in elfInstructions.txt
# ^ = North
# v = South
# > = East
# < = West
# Starting house gets a present (arbitrarily chosen (0,0) for starting house)
# Part 1: find out how many houses get >=1 present
# Part 2: if Santa and Robo-Santa use alternating instructions, how many houses get >= 1 present

import numpy
def how_many_houses(instructions,nSantas):
    # create matrix where col1,col2 = x,y and rows correspond to the number of Santas
    currentHouse = numpy.zeros((nSantas,2))
    # map to store coordinates of visited houses
    houses = [(0,0)]
    Santa = 0
    for word in instructions:
        for ch in word:
            # use modulo to make sure we cycle through the Santas
            Santa = (Santa+1) % nSantas
            if ch == '^':
                currentHouse[Santa][0]+=1
            elif ch == 'v':
                currentHouse[Santa][0]-=1
            elif ch == '<':
                currentHouse[Santa][1]-=1
            elif ch == '>':
                currentHouse[Santa][1]+=1
            else:
                print 'Warning: unclear instruction:"{}", skipping.'.format(ch)
            if (currentHouse[Santa][0],currentHouse[Santa][1]) not in houses:
                houses.append((currentHouse[Santa][0],currentHouse[Santa][1]))
    print 'For {} Santas, {} houses receive at least one present'.format(nSantas,len(houses))
    
if __name__ == "__main__":
    instructions_file = open('elfInstructions.txt')
    instructions = instructions_file.read()
    instructions_file.close()
    how_many_houses(instructions,1)
    how_many_houses(instructions,2)
