# Day 8
# Part 2
# counting the difference between the code length and the strings once
# we convert:
# " = \"
# \" = \\\",
# \\ = \\\\,
# \xnn = \\xnn
import string

input = open('input.txt')
count = 0
for line in input:
    Line = line.rstrip('\n')
    search = Line.find('\\')
    currentCount = 4
    while search > -1:
        # end of Line
        if search == (len(Line) - 2):
            search = -1
        # \" or \\    
        elif (Line[search+1] == '"') or (Line[search+1] == '\\'):
            #print '\\" or \\\\ at {}'.format(search)
            currentCount += 2
            search = Line.find('\\',search+2)
        # \xnn (must be more then 4 characters form the end)
        elif Line[search+1] == 'x' and Line[search+2] in string.hexdigits and Line[search+3] in string.hexdigits:
            #print 'a hex upon your house at {}'.format(search)
            currentCount += 1 
            search = Line.find('\\',search+4)
        else: # single \
            search = Line.find('\\',search+1)
    count+=currentCount
    #print currentMem,memCount
print 'difference = {}'.format(count)
