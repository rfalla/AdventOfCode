# Input is a list of cups which are aranged in a clockwise circle.
# Each move:
# The next 3 cups are removed from the circle.
# The destination cup is the next highest cup in the remaining circle, if your current cup is the smallest then it wraps around to the max.
# The 3 cups that were previously picked up are put after the destination cup.
# The next current cup is one to the right of the current cup.
# Part 1: After 100 moves, what is the order of the cups (starting to the right of 1 and not including it)?
# Part 2: There are 1M cups - numbered from 1-1M, with the ordering going puzzle input, then max(puzzle input)+1 ascending.
# After 10M moves, what is the product of the two moves after cup 1?
#
# Using a dictionary (cups_dict) to simulate a circular singly-linked list with current as the head.
def play(cups_dict, current, moves, max_cup, part2=False):
    for i in range(moves):
        cups_dict = move(cups_dict, current, max_cup)
        current = cups_dict[current]
    if part2:
        return product_of_next(cups_dict)
    else:
        return order_cups(cups_dict)

def move(cups_dict, current, max_cup):
    cups_to_move = []
    next = current
    #find cups to move
    for i in range(3):
        next = cups_dict[next]
        cups_to_move.append(next)
    # find destination
    next = current
    for i in range(4):
        next-=1
        if next < 1:
            next = max_cup
        if next not in cups_to_move:
            break
    # current now points to next cup after the 3 to move
    cups_dict[current] = cups_dict[cups_to_move[-1]]
    end_of_chain = cups_dict[next]
    # the destination cup points to the start of the cups to move
    cups_dict[next] = cups_to_move[0]
    # the final cup to move points to what the destination used to point to
    cups_dict[cups_to_move[-1]] = end_of_chain
    return cups_dict

def order_cups(cups_dict, order_from=1):
    string_input = []
    next = cups_dict[order_from]
    while True:
        if next == order_from:
            break
        string_input.append(str(next))
        next = cups_dict[next]
    return''.join(string_input)

def product_of_next(cups_dict, order_from=1, nproduct=2):
    output = 1
    for i in range(nproduct):
        order_from = cups_dict[order_from]
        output*=order_from
    return output

input = [5,9,8,1,6,2,7,3,4]
len_input = len(input)
cups_dict = {}
for i in range(len_input):
    cups_dict[input[i]] = input[(i+1)%len_input]
print('Part 1: {}'.format(play(cups_dict, input[0], 100, 9)))

cups_dict = {}
for i in range(len_input-1):
    cups_dict[input[i]] = input[i+1]
# I did trial not bothering with 10->1e6 and using the .get function defaulting to key+1
# but due to the number of moves all ints get used anyway, so implementing here and doing direct search is quicker than .get()
for i in range(len_input+1,int(1e6)):
    cups_dict[i] = i+1
cups_dict[input[-1]] = len_input+1
cups_dict[int(1e6)] = input[0]
print('Part 2: {}'.format(play(cups_dict, input[0], int(1e7), int(1e6), True)))
