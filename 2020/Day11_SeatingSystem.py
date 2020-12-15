# Part 1: input is a seating layout with:
#    . -> floor
#    L -> empty seat
#    # -> occupied seat
# Each run changes:
#    L -> # if all adjacent seats (up, down, left, right, diagonals) are L.
#    # -> L if at least 4 adjacent seats are #.
# After some time the seating arrangement will stabilise, how many seats are occupied when this happens?

def seat_next(seating_dict, neighbours_dict, key, tolerance):
    count = 0
    for n in neighbours_dict[key]:
        count+=seating_dict[n]
        if count > 0 and seating_dict[key] == 0:
            return 0
        elif count > tolerance and seating_dict[key] == 1:
            return 0
    return 1

def find_stable_seats(seating_dict, neighbours_dict, tolerance):
    while True:
        next_seating_dict = {}
        for key in seating_dict:
            next_seating_dict[key] = seat_next(seating_dict, neighbours_dict, key, tolerance)
        if next_seating_dict == seating_dict:
            return sum(seating_dict.values())
        else:
            #if tolerance == 4:
                #print()
                #print(seating_dict)
            seating_dict = next_seating_dict.copy()

def find_neighbours(seating_dict, key, x0, xmax, y0, ymax):
    x=x0
    y=y0
    while key[0]+x > -1 and key[0]+x < xmax and key[1]+y > -1 and key[1]+y < ymax:
        if (key[0]+x, key[1]+y) in seating_dict:
            return key[0]+x, key[1]+y
        x+=x0
        y+=y0
    return None

# filling complete border with floor to avoid edges
seating_area = [x.strip('\n').replace('L','#') for x in open('input_11.txt')]
seating_dict = {}
for i in range(len(seating_area)):
    for j in range(len(seating_area[0])):
        if seating_area[i][j] == 'L':
            seating_dict[i,j] = 0
        elif seating_area[i][j] == '#':
            seating_dict[i,j] = 1

neighbours_part1 = {}
neighbours_part2 = {}
xmax = len(seating_area)
ymax = len(seating_area[0])
for key in seating_dict:
    neighbours_part1[key] = []
    neighbours_part2[key] = []
    for i in range(-1,2):
        for j in range(-1,2):
            if i == 0 and j == 0:
                continue
            if (key[0]+i, key[1]+j) in seating_dict:
                neighbours_part1[key].append((key[0]+i,key[1]+j))
            next_neighbour = find_neighbours(seating_dict, key, i, xmax, j, ymax)
            if not next_neighbour is None:
                neighbours_part2[key].append(next_neighbour)

print('Part 1: {}, Part 2: {}'.format(find_stable_seats(seating_dict, neighbours_part1, 3)\
                                      , find_stable_seats(seating_dict, neighbours_part2, 4)))
