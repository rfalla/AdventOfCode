# Day 2
# Part 1: count how many passwords are valid
# input is of the form "n-m i: xyz" where:
# xyz > password
# n-m i > password must contain i between n & m times (inclusive)
#
# Part 2: same input but new rules.
# n & m are now positions to look for the character i, index 1.
# A password is valid if there is 1 match
import re

def unpick_input(input):
    return re.search('(\d+)-(\d+) ([a-z]): ([a-z]+)',input)

def part1(input):
    count_of_string = input.group(4).count(input.group(3))
    if count_of_string >= int(input.group(1)) and count_of_string <= int(input.group(2)):
        return 1
    return 0

def part2(input):
    pos1 = input.group(4)[int(input.group(1))-1]
    pos2 = input.group(4)[int(input.group(2))-1]
    return (pos1 == input.group(3)) ^ (pos2 == input.group(3))

raw_input = [unpick_input(line) for line in open('input_02.txt')]
part1_list = [part1(x) for x in raw_input]
part2_list = [part2(x) for x in raw_input]
print('Part 1: {}, Part 2: {}'.format(sum(part1_list),sum(part2_list)))
