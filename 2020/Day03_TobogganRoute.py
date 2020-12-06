# Day 2
# Part 1: input is a nx11 grid containing {.,#} which repeats infinitely
# starting top left, go right 3, down 1.
# count the number of # that you encounter on this route.
#
# Part 2: count the number of trees encountered for the following routes:
# Right 1, down 1.
# Right 3, down 1. (Part 1)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
#
# Not too happy with my code here, could be more pythonic with how I choose x
# (Next day) found proper mod way to set x!
from numpy import prod
raw_input = [line.strip('\n') for line in open('input_03.txt')]

def CountTrees(input, right, down):
    counter, x = 0, 0
    len_mod = len(raw_input[0])

    for i in range(0,len(input),down):
        if input[i][x] == '#':
            counter+=1
        #x+=right
        #if x>len_mod-1:
        #    x-=len_mod
        x = (x+right) % (len_mod)
    return counter

routes_to_test = [[1,1],[3,1],[5,1],[7,1],[1,2]]
print('Part 1: {}, Part 2: {}'.format(CountTrees(raw_input,3,1), prod([CountTrees(raw_input,x[0],x[1]) for x in routes_to_test])))
