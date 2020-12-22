# Part 1: Memory game where numbers are said based on previous numbers...
# First state the starting numbers.
# Then each go is based on the previous number - if it was new then 0, if not, the number of goes since it was last said.
# What is the 2020th number?
# What is the 30000000th number?
# Quite slow for part 2 but didn't require any refactoring! takes <20s to run.
input = [6,3,15,13,1,0]
used_numbers = {val: i+1 for i, val in enumerate(input)}
previous_number = input[-1]
for i in range(len(used_numbers)+1,30000000):
    used_numbers[previous_number], previous_number = i, i - used_numbers.get(previous_number,i)
    if i == 2019:
        print('Part 1: {}'.format(previous_number))
print('Part 2: {}'.format(previous_number))
