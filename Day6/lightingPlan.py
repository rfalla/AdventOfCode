# Day 6
# have lights in a 1000x1000 grid
# given instructions by santa on how to light them
# instructions are bottom LH corner to top RH corner inclusive
# work out how many are lit at the end

import numpy
def findCorners(line_nostart):
    corners = line_nostart.split(' through ')
    corner1 = corners[0].split(',')
    x1 = int(corner1[0])
    y1 = int(corner1[1])
    corner2 = corners[1].split(',')
    x2 = int(corner2[0])+1 # inclusive
    y2 = int(corner2[1])+1 # inclusive
    return [x1,y1,x2,y2]

def turnOn(grid,corners):
    # 0->1, 1->1
    newLightsOn = numpy.ones((corners[2]-corners[0],corners[3]-corners[1]))
    grid[corners[0]:corners[2],corners[1]:corners[3]] = newLightsOn

def toggle(grid,corners):
    # 0->1, 1->0
    grid[corners[0]:corners[2],corners[1]:corners[3]] = (numpy.ones((corners[2]-corners[0],corners[3]-corners[1]))-grid[corners[0]:corners[2],corners[1]:corners[3]])
    
def turnOff(grid,corners):
    # 0->0, 1->0
    newLightsOff = numpy.zeros((corners[2]-corners[0],corners[3]-corners[1]))
    grid[corners[0]:corners[2],corners[1]:corners[3]] = newLightsOff
    
if __name__ == "__main__":
    
    instructions = open('input.txt')
    grid = numpy.zeros((1000,1000))
    for line in instructions:
        if line.startswith('turn on'):
            line_nostart = line[8:]
            corners = findCorners(line_nostart)
            turnOn(grid,corners)
        elif line.startswith('toggle'):
            line_nostart = line[7:]
            corners = findCorners(line_nostart)
            toggle(grid,corners)
        elif line.startswith('turn off'):
            line_nostart = line[9:]
            corners = findCorners(line_nostart)
            turnOff(grid,corners)
        else:
            print 'Error: unclear instructions: {}'.format(line)
    print 'There are {} lights on'.format(grid.sum())
