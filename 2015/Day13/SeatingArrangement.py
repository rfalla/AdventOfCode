# Day 13
# Travelling salesman problem
# Only 8 houses so using brute force
# using permutations tool from itertools
###########
# code stolen from Day 9
# modified since A->B != B-A
# Added myself in for Part 2

from itertools import permutations

def total_happiness(options,order):
    hap = 0
    for i in range(len(order)-1):
        hap += options[order[i],order[i+1]]
        hap += options[order[i+1],order[i]]

    hap += options[order[0],order[-1]]
    hap += options[order[-1],order[0]]
    return hap

if __name__ == '__main__':
    input = open('input.txt')
    options = {}
    people = []
    for line in input:
        line_strip = line.rstrip()
        words = line_strip.split(' ')
        if words[2] == 'gain':
            options[words[0],words[10][:-1]] = int(words[3])
        else:
            options[words[0],words[10][:-1]] = -1*int(words[3])
        if words[0] not in people:
            people.append(words[0])
            options[words[0],'me'] = 0
            options['me',words[0]] = 0
    people.append('me')
    input.close()

    smallHappy = 10000000
    bigHappy = 0
    for perm in permutations(people):
        hap = total_happiness(options,list(perm))
        if hap < smallHappy:
            smallHappy = hap
            print 'smallest happiness so far: {}'.format(list(perm))
        if hap > bigHappy:
            bigHappy = hap
            print 'largest happiness so far: {}'.format(list(perm))
    print smallHappy,bigHappy
