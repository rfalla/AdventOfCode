# Part 1, find pair of numbers that sum to 2020, multiply for answer
# Part 2, find triplet of numbers that sum to 2020, multiply for answer

# After looking at other people's solutions I am happy with my go. Most other python answers are using brute force.
# Good variants on this solution use itertools.combinations, e.g.
# print ("part two = ",  [a* b * c for (a, b, c) in  itertools.combinations(nums, 3) if a + b + c == 2020][0])

# Extensions to code would be ensuring it's not repeating a number (e.g. if element n in raw_input = 1010 then the
# code would currently produce that as the answer but it would only be valid if there was another element m = 1010.
raw_input = [int(line.rstrip('\n')) for line in open('input_01.txt')]
dict_input = dict.fromkeys(raw_input,1)
inverse_input = [2020 - x for x in raw_input]
for i in inverse_input:
    if i in dict_input:
        print('Part 1: {}'.format(i*(2020-i)))
        break

dict_sum_input = {}
for i in range(len(raw_input)):
    for j in range(i+1,len(raw_input)):
        dict_sum_input[raw_input[i] + raw_input[j]] = raw_input[i]*raw_input[j]

for i in inverse_input:
    if i in dict_sum_input:
        print('Part 2: {}'.format((2020-i)*dict_sum_input[i]))
        break
