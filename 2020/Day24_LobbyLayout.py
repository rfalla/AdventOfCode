# Hexagonal grid of tiles in 0/1 state.
# All tiles start in off state.
# Input is a list of tiles that need to be flipped.
# Each line is a list of directions from a reference grid.
# Each line has no delimeters, directions are e, se, sw, w, nw, ne, so e.g. esenee = e, se, ne, e
# Part 1: after processing, how many tiles are in the on state?
# After reading through this helpful website https://www.redblobgames.com/grids/hexagons/ I'm going to use axial coordinates.
# Also picked up the idea for using complex numbers for the two coordinates off reddit (was originally using np.arrays and storing as tuples).
# Part 2: Each day the tiles are flipped according to these rules:
#    Any on tile with zero or more than 2 on tiles immediately adjacent to it is flipped to off.
#    Any off tile with exactly 2 on tiles immediately adjacent to it is flipped to on.
# How many tiles are on after 100 days?
def setup_tiles(directions_dict, input):
    tiles = set()
    for line in input:
        two_digit = False
        tile = 0+0j
        for i in range(len(line)):
            if two_digit:
                tile += directions_dict[line[i-1:i+1]]
                two_digit = False
            else:
                if line[i] in ['s','n']:
                    two_digit = True
                else:
                    tile += directions_dict[line[i]]
        if tile in tiles:
            tiles.remove(tile)
        else:
            tiles.add(tile)
    return tiles

def flip_tiles(directions, tiles):
    next_on = set()
    off_checked = set()
    for tile in tiles:
        temp_new_on, temp_off_checked = check_flip_tile(directions, tiles, off_checked, tile, 1)
        next_on |= temp_new_on
        off_checked |= temp_off_checked
    return next_on

def check_flip_tile(directions, tiles, off_checked, tile, status):
    count = 0
    new_on = set()
    if status == 0:
        off_checked.add(tile)
    for coord in set([tile+x for x in directions]):
        if coord in tiles:
            count+=1
        elif coord not in off_checked and status == 1:
            temp_new_on, temp_off_checked = check_flip_tile(directions, tiles, off_checked, coord, 0)
            new_on |= temp_new_on
            off_checked |= temp_off_checked
    if status and (count == 1 or count == 2):
        new_on.add(tile)
    elif not status and count == 2:
        new_on.add(tile)
    return new_on, off_checked

def main():
    directions_dict = {'e': 1, 'se': 1j, 'sw': -1+1j, 'w': -1, 'nw': -1j, 'ne': 1-1j}
    input = [x.strip('\n') for x in open('input_24.txt')]
    tiles = setup_tiles(directions_dict, input)
    print('Part 1: {}'.format(len(tiles)))
    for i in range(100):
        tiles = flip_tiles(directions_dict.values(), tiles)
    print('Part 2: {}'.format(len(tiles)))

main()
