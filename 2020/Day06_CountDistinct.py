# Part 1: Count distinct letters per group
# Part 2: Count common letters per group
from functools import reduce
answers = [chunk.split() for chunk in open("input_06.txt").read().split("\n\n")]
count_distinct = sum([len(set(''.join(x))) for x in answers])
count_common = sum([len(reduce(lambda a, b: set(a) & set(b), x)) for x in answers])
print('Part 1: {}, Part 2: {}'.format(count_distinct, count_common))
