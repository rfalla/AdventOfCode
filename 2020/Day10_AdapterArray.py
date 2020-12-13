# Part 1: joltage adapters are rated for a specific output joltage (input). Any given adapter can take input 1-3 jolts lower than its rating.
# Your device has a built-in joltage adapter rated for 3 jolts higher than the highest-rated adapter in your bag.
# The charger has an effective joltage rating of 0.
# Using every adapter in the list what is the number of 1-jlt differences multiplied by the number of 3-jolt differences?
#
# Part 2: count how many distinct chains of adapters can connect the charger to your device. Hint: There are over a trillion so do not use brute force! 
import numpy as np
from itertools import combinations

def find_differences(input):
    input.sort()
    shift_input = input[1:]
    return shift_input - input[0:-1]

def find_combinations(input):
    # Find numbers which are essential in the list - this will be numbers where the difference = 3
    essentials_pos = [x for x in range(len(differences)) if differences[x] == 3]
    # The max element in raw_input is essential
    essentials_pos.append(len(raw_input)-1)
    multiplier = 1
    previous = 0
    # Breaking down the chain into chunks split up by essential elements.
    # Then the total number of chains is the number possible in each chain mulitplied together.
    for i in essentials_pos:
        nComb = 0
        if i-previous >= 2:
            input_to_combine = input[previous:i]
            for j in range(len(input_to_combine)):
                for k in combinations(input_to_combine,j+1):
                    potential_list = np.asarray(k)
                    potential_list = np.insert(potential_list, -1, input[i])
                    if previous > 0:
                        potential_list = np.insert(potential_list, 0, input[previous-1])
                    else:
                        potential_list = np.insert(potential_list, 0, 0)
                    if max(find_differences(potential_list)) < 4:
                        nComb+=1
            multiplier*=max(1,nComb)
        previous = i+1
    return multiplier

raw_input = np.array([int(x.strip('\n')) for x in open('input_10.txt')])
differences = find_differences(raw_input)
print('Part 1: {}'.format((1 + np.count_nonzero(differences == 1))*(1 + np.count_nonzero(differences == 3))))

# Find numbers which are essential in the list - this will be numbers where the difference = 3
essentials_pos = [x for x in range(len(differences)) if differences[x] == 3]
# The max element in raw_input is essential
essentials_pos.append(len(raw_input)-1)
print('Part 2: {}'.format(find_combinations(raw_input)))
