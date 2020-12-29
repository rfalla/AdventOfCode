# Input is a list of square tiles.
# Need to rearrange the tiles (rotate and/or flip) so that they create a grid where the inside tiles match.
# Part 1: Multiply the corner IDs.
#
# Now that we know the arrangement of tiles we can check the image for sea monsters.
# First remove all borders from tiles.
# Sea minsters look like:
#---------------------|
#|                  # |
#|#    ##    ##    ###|
#| #  #  #  #  #  #   |
#---------------------|
# The blanks can be . or #.
# You may need to flip/rotate the board to find the monsters.
# Part 2: How many # are not part of a sea monster?
#
# NOTES: This code is not optimised AT ALL, it is so slow and ugly but I am bored of this puzzle so moving onto day 21!
from functools import reduce
import numpy as np
from collections import defaultdict
def parse(filename):
    tiles_raw = [x.strip('\n').split('\n') for x in open(filename).read().split("\n\n")]
    tiles = {}
    for tile in tiles_raw:
        id = int(tile[0][5:-1])
        tiles[id] = np.array([list(x) for x in tile[1:]])
    return tiles

def find_tile_alternates(tile):
    tiles = []
    tiles.append(tile)
    tiles.append(np.rot90(tile,1))
    tiles.append(np.rot90(tile,2))
    tiles.append(np.rot90(tile,3))
    tiles.append(np.fliplr(tile))
    tiles.append(np.rot90(tiles[-1]))
    tiles.append(np.rot90(tiles[-1]))
    tiles.append(np.rot90(tiles[-1]))
    return tiles

def assemble_grid(tiles, grid=None, used=set()):
    matches = defaultdict(list)
    size = int(len(tiles)**0.5)#square grid
    if grid is None:
        grid = [[dict() for y in range(size)] for x in range(size)]
    for r in range(size):
        for c in range(size):
            if len(grid[r][c]) > 0:
                continue
            for tile_id in tiles:
                if tile_id in used:
                    continue
                for t in find_tile_alternates(tiles[tile_id]):
                    # check above
                    if r > 0:
                        current_top = t[0]
                        above_bottom = grid[r-1][c]['tile'][-1]
                        if not np.array_equal(current_top, above_bottom):
                            continue
                    # check left
                    if c > 0:
                        current_left = t[:, 0]
                        left_right = grid[r][c-1]['tile'][:, -1]
                        if not np.array_equal(current_left, left_right):
                            continue
                    grid[r][c]['id'] = tile_id
                    grid[r][c]['tile'] = t
                    used.add(tile_id)
                    recursive_result = assemble_grid(tiles, grid, used)
                    if not recursive_result is None:
                        return recursive_result
                    grid[r][c] = {}
                    used.remove(tile_id)
            if len(grid[r][c]) == 0:
                return None
    return grid

def remove_borders_and_join(grid):
    new_size = len(grid[0][0]['tile'])-2
    new_grid = np.chararray((new_size*len(grid), new_size*len(grid)), unicode=True)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            new_grid[r*new_size:(r+1)*new_size, c*new_size:(c+1)*new_size] = grid[r][c]['tile'][1:-1, 1:-1]
    return new_grid

def find_monsters(grid, monster):
    grid_options = find_tile_alternates(grid)
    nMonsters = 0
    for g in grid_options:
        for r in range(len(g)-2):#monster can't be off the edge of the grid
            for c in range(len(g[0])-19):#monster can't be off the edge of the grid
                found_monster = True
                for m in monster:
                    try:
                        if g[r+m[0]][c+m[1]] != '#':
                            found_monster = False
                            continue
                    except:
                        found_monster = False
                if found_monster:
                    nMonsters+=1
        if nMonsters>0:
            return nMonsters
    return nMonsters
                
if __name__=="__main__":
    tiles = parse('input_20.txt')
    grid = assemble_grid(tiles)
    part1 = grid[0][0]['id']*grid[0][len(grid)-1]['id']*grid[len(grid)-1][0]['id']*grid[len(grid)-1][len(grid)-1]['id']
    grid = remove_borders_and_join(grid)
    monster = [[0,18],[1,0],[1,5],[1,6],[1,11],[1,12],[1,17],[1,18],[1,19],[2,1],[2,4],[2,7],[2,10],[2,13],[2,16]]
    nMonsters = find_monsters(grid, monster)
    part2 = np.count_nonzero(grid == '#') - nMonsters*len(monster)
    print('Part 1: {}, Part 2: {}'.format(part1,part2))
