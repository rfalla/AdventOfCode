# Day 12
# input is file containing JSON
# count all numbers in it
# don't include objects which contain "red"
# this way is much better than Part 1
# less code!
# to obtain Part 1 answer comment out l14 & l15
################################

import json

def sum_file(f):
    if isinstance(f,dict):
        if "red" in f.values():
            return 0
        return sum(map(sum_file, f.values()))
    if isinstance(f,list):
        return sum(map(sum_file, f))
    if isinstance(f,int):
        return f
    return 0

if __name__ == "__main__":
    input = json.loads(open('input.txt', 'r').read())
    print 'Total = {}'.format(sum_file(input))
