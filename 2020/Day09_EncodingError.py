# Part 1: find first number in list that cannot be made from sum of previous n numbers.
# Part 2: find a contingious list of numbers which sum to the answer to Part 1, return the sum of the smalled and largest numbers.
def add_to_allowed(de, x, y):
    if x == y:
        de.append(-99)
    else:
        de.append(x+y)
    return de

def recursive_sum(x, num_list, pos, target, current_list):
    x += num_list[pos]
    current_list.append(num_list[pos])
    if x < target:
        return recursive_sum(x, num_list, pos+1, target, current_list)
    else:
        return current_list

import collections
num_list = [int(x.strip('\n')) for x in open('input_09.txt')]
preamble = 25
de_allowed = collections.deque()
for i in range(preamble):
    for j in range(preamble):
        de_allowed = add_to_allowed(de_allowed, num_list[i], num_list[j])

for i in range(preamble, len(num_list)):
    new_num = num_list[i]
    if new_num not in de_allowed:
        break
    for j in range(preamble):
        de_allowed.popleft()
        de_allowed = add_to_allowed(de_allowed, new_num, num_list[i-preamble+j])

part2 = [min(x)+max(x) for x in [recursive_sum(0, num_list, x, new_num, []) for x in range(len(num_list))] if sum(x) == new_num][0]
print('Part 1: {}, Part 2: {}'.format(new_num, part2))
