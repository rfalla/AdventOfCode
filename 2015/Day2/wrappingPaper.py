# Day 2
# Given present dimensions in presents.txt in format 1x2x3
# Part 1: work out how much wrapping paper is needed
# - for each present need surface area of box + smallest side area
# Paer 2: work out how much ribbon is needed
# - for each present need volume of box + 2*(smallest side + 2nd smallest side)
presents = open('presents.txt')
total_paper = 0
total_ribbon = 0
for line in presents:
    lengths = line.split('x')
    lengths = [int(x) for x in lengths]
    lengths.sort()
    lw = lengths[0]*lengths[1]
    wh = lengths[1]*lengths[2]
    lh = lengths[0]*lengths[2]
    total_paper += 2*(lw + wh + lh)
    total_paper += lengths[0]*lengths[1]
    volume = lengths[0]*lengths[1]*lengths[2]
    total_ribbon += volume
    total_ribbon += 2*(lengths[0] + lengths[1])
print 'The total amount of wrapping paper needed is {} square feet'.format(total_paper)
print 'The total length of ribbon needed is {} feet'.format(total_ribbon)
