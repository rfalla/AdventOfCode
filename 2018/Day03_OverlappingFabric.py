# Part 1: rectangle of fabric instructions come in the form
# #id @ l,t: wxh
# where l,t are the distance from the left and top edge
# w and h are the width and height of the rectangle
#
# Count how many square inches of fabric have overlapping claims
#
# Part 2: only one order doesn't overlap, what is this order?

# IMPROVEMENTS: use orders = [[*map(int, re.findall(r'\d+', x))] for x in open('input_03.txt')] instead of manaually using int() for each variable
# then don't need to use global variables because can perform remainder on orders (list of orders)
import re

coords = {}
unique_ids = {}
def process_order(input):
    order = re.search('\#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)',input)
    #print(order.group(0), order.group(1), order.group(2), order.group(3), order.group(4), order.group(5))
    id, left, top, width, height = int(order.group(1)), int(order.group(2)), int(order.group(3)), int(order.group(4)), int(order.group(5))
    unique_id = True
    for i in range(left, left+width):
        for j in range(top, top+height):
            #print('x = {}, y = {}'.format(left+i, top+j))
            coord = str(i) + ',' + str(j)
            if coord in coords:
                unique_ids.pop(coords[coord], None)
                coords[coord] = -1
                unique_id = False
            else:
                coords[coord] = id
    if unique_id == True:
        unique_ids[id] = 1


[process_order(x.strip('\n')) for x in open('input_03.txt')]
print('Part 1: {}, Part 2: {}'.format(sum([1 for x in coords if coords[x] == -1]), unique_ids.keys()[0]))
