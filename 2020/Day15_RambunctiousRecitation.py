# Part 1: Memory game where numbers are said based on previous numbers...
# First state the starting numbers.
# Then each go is based on the previous number - if it was new then 0, if not, the number of goes since it was last said.
# What is the 2020th number?
# What is the 30000000th number?
# Quite slow for part 2 but didn't require any refactoring! takes <1min to run.
used_numbers = {6:1,3:2,15:3,13:4,1:5}
previous_number = 0
for i in range(len(used_numbers)+1,30000000):
    if previous_number in used_numbers:
        current_number = i - used_numbers[previous_number]
    else:
        current_number = 0
    used_numbers[previous_number] = i
    if i == 2020:
        print('Part 1: {}'.format(previous_number))
    previous_number = current_number
print('Part 2: {}'.format(previous_number))
