# Part 1: go through list of boarding passes and calculate seat ID, return max seat ID.
# plane has 127x7 seats
# boarding passes like FBFBBFFRLR
# use bisection to find seat:
#     chars 0 to 6 indicate row, F = front half, B = bottom half
#     chars 7-9 indicate column, L = left half, R = right half
# then Seat ID = 8r + c
#
# Part 2: find your seat!
# It should be missing from the list of seats, but the seat before and after will be present.
#
# After looking at other answers:
# HOLY SMOKES! You can find the seat_id from int(boarding pass, 2) as long as you convert F/L->0, B/R -> 1
# Using that method we can update seat_ids to:
# seat_ids = [int(line.strip('\n').replace('F','0').replace('B','1'),replace('L','0').replace('R','1'),2) for line in open('input_05.txt')]
# and do away with both of the functions.
def find_position(str_to_check, lower, upper):
    new_size = (upper-lower)/2
    if str_to_check[0] == 'F':
        upper = lower + new_size
    else:
        lower = upper - new_size
    if lower == upper:
        return lower
    else:
        return find_position(str_to_check[1:], lower, upper)
        

def find_seat_id(input):
    row = find_position(input[:7],0,127)
    column = find_position(input[7:].replace('L','F').replace('R','B'),0,7)
    return row*8+column

seat_ids = [find_seat_id(line.strip('\n')) for line in open('input_05.txt')]
max_seat_id = max(seat_ids)
min_seat_id = min(seat_ids)
sum_seat_ids = sum(seat_ids)
# Using some maths we can work out what number is missing.
# The sum of ints from a to b = (b-a+1)(a+b)/2
missing_seat = (max_seat_id-min_seat_id+1)*(min_seat_id+max_seat_id)/2
missing_seat -= sum_seat_ids
print('Part 1: {}, Part 2: {}'.format(max_seat_id,missing_seat))
