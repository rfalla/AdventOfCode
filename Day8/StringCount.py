# Day 8
# counting the code length - memory length for a list of strings
# watch out for \", \\, \xnn, these all are equal to 1 in mem length
# mem length doesn't include the first and last " in each string
import string

input = open('input.txt')
codeCount = 0
memCount = 0
for line in input:
    Line = line.rstrip('\n')
    codeCount += len(Line)
    search = Line.find('\\')
    currentMem = len(Line) - 2
    #print Line
    while search > -1:
        # end of Line
        if search == (len(Line) - 2):
            search = -1
        # \" or \\    
        elif (Line[search+1] == '"') or (Line[search+1] == '\\'):
            #print '\\" or \\\\ at {}'.format(search)
            currentMem -= 1
            search = Line.find('\\',search+2)
        # \xnn (must be more then 4 characters form the end)
        elif Line[search+1] == 'x' and Line[search+2] in string.hexdigits and Line[search+3] in string.hexdigits:
            #print 'a hex upon your house at {}'.format(search)
            currentMem -= 3
            search = Line.find('\\',search+4)
        else: # single \
            search = Line.find('\\',search+1)
    memCount+=currentMem
    #print currentMem,memCount
print 'codeCount = {0}, memCount = {1}, difference = {2}'.format(codeCount,memCount,codeCount-memCount)
