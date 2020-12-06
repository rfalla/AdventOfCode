
# Part 1, count the number of IDs containing exactly two of any letter and then separately counting those with exactly three of any letter.
# Multiply those two counts together to get a rudimentary checksum
#
# Part 2, find two strings in input that only differ by one character, print out matching characters
import numpy as np
def check_sum(input):
    check2, check3 = False, False
    for ch in set(input):
        if input.count(ch) == 2:
            check2 = True
        elif input.count(ch) == 3:
            check3 = True
    return [check2, check3]

part1_input = [check_sum(line.rstrip('\n')) for line in open('input_02.txt')]
part1_output = [sum(i) for i in zip(*part1_input)] 
print('Part 1: {}'.format(part1_output[0]*part1_output[1]))

part2_input = [line.rstrip('\n') for line in open('input_02.txt')]
for i in range(len(part2_input)-1):
    for j in range(i+1,len(part2_input)):
        counter = -1
        for k in range(len(part2_input[i])):
            if part2_input[i][k] != part2_input[j][k]:
                if counter != -1:
                    break
                counter = k
        else:
            print('Part 2: {}'.format(part2_input[i][:counter]+part2_input[i][counter+1:]))
            break
