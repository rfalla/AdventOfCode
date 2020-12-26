# 3-d infinite grid where each discrete coordinate represents a cube which is on(#)/off(.).
# At t=0 all cubes inactive except for those in puzzle input.
# On each cycle, each cube considers its nearest neighbours.
# If a cube is active and exactly 2 or 3 neighbours are also active it remains active, otherwise inactive.
# If the cube is inactive and exactly 3 of its neighbours are active it becomes active, otherwise inactive.
# Part 1: after 6 cycles, how many cubes are left active?
# Part 2: Upgrade to 4-d, after 6 cycles how many cubes are left active?
#
# There is definitely a way to generalise this to n-dimensions, but I haven't figured out how to add in the symmetry shortcuts for n-dimensions so have left it as 2 functions.
from itertools import product
def next_3d(active_cubes, empties_checked, cube, status):
    count = 0
    new_active = set()
    if status == 0:
        empties_checked.add(cube)
    for coord in set(product(*[range(x-1, x+2) for x in cube])):
        if coord == cube:
            continue
        # No need to bother with z<0 due to symmetry
        if coord[2] < 0:
            continue
        if coord in active_cubes:
            count+=1
            # Since we start with no active cubes in the z plane active cells will be symmetric around z.
            if coord[2]>0 and cube[2] == 0:
                count+= 1
        elif coord not in empties_checked and status == 1:
            temp_new_active, temp_empties_checked = next_3d(active_cubes, empties_checked, coord, 0)
            new_active |= temp_new_active
            empties_checked |= temp_empties_checked
    if status == 1 and (count == 2 or count == 3):
        new_active.add(cube), empties_checked
    elif status == 0 and count == 3:
        new_active.add((cube[0], cube[1], cube[2]))
    return new_active, empties_checked

def next_4d(active_cubes, empties_checked, cube, status):
    count = 0
    new_active = set()
    if status == 0:
        empties_checked.add(cube)
    for coord in set(product(*[range(x-1,x+2) for x in cube])):
        if coord == cube:
            continue
        # since z and w are interchangeable, making the decision to work in the phase-space where z <= w.
        coord = (coord[0], coord[1], min(abs(coord[2]), abs(coord[3])), max(abs(coord[2]), abs(coord[3])))
        if coord in active_cubes:
            count+=1
        elif coord not in empties_checked and status == 1:
            temp_new_active, temp_empties_checked = next_4d(active_cubes, empties_checked, coord, 0)
            new_active |= temp_new_active
            empties_checked |= temp_empties_checked
    if status == 1 and (count == 2 or count == 3):
        new_active.add(cube), empties_checked
    elif status == 0 and count == 3:
        new_active.add(cube)
    return new_active, empties_checked

def cycle(active_cubes, dim):
    next_cubes = set()
    empties_checked = set()
    for cube in active_cubes:
        if dim == 3:
            temp_new_active, temp_empties_checked = next_3d(active_cubes_3d, empties_checked, cube, 1)
        elif dim == 4:
            temp_new_active, temp_empties_checked = next_4d(active_cubes_4d, empties_checked, cube, 1)
        next_cubes |= temp_new_active
        empties_checked |= temp_empties_checked
    return next_cubes

if __name__=="__main__":
    nCycles = 6
    input = [x.strip('\n') for x in open('input_17.txt')]
    active_cubes_3d = set()
    active_cubes_4d = set()
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == '#':
                active_cubes_3d.add((i,j,0))
                active_cubes_4d.add((i,j,0,0))

    for i in range(nCycles):
        active_cubes_3d = cycle(active_cubes_3d, 3)
        active_cubes_4d = cycle(active_cubes_4d, 4)
    
    # 0->1
    # n-> n, -n ->2
    part1 = sum([1 for x in active_cubes_3d if x[2]==0]) + sum([2 for x in active_cubes_3d if x[2] > 0])
    # 00 ->1
    # 0n ->0n,0-n, n0, -n0 ->4
    # nn ->nn, n-n, -n-n, -nn ->4
    # nm ->nm, -nm, n-m, -n-m, mn, m-n, -mn, -m-n ->8
    part2 = sum([1 for x in active_cubes_4d if x[2]==0 and x[3]==0]) \
            + sum([4 for x in active_cubes_4d if (x[2]==0 and x[3]>0) or (x[2]>0 and x[3]==0)]) \
            + sum([4 for x in active_cubes_4d if x[2]>0 and x[2]==x[3]]) \
            + sum([8 for x in active_cubes_4d if x[2]!=x[3] and x[2]>0 and x[3]>0])
    print('Part 1: {}, Part 2: {}'.format(part1, part2))
