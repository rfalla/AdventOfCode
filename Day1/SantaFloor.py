# Day 1
# input stored in floors.txt
# ( = go up a floor
# ) = go down a floor
# Part 1: find out what floor he ends up on
# Part 2: find out at what instruction he first enters the basement (floor = -1)
# start on floor 0
################################

floors = open('floors.txt')
floor = 0
count = 1
entered_basement = False
for word in floors:
    for ch in word:
        if ch == '(':
            floor += 1
        elif ch == ')':
            floor -= 1
        else:
            print 'unclear instruction, skipping.'
        if entered_basement == False and floor == -1:
            print 'He first enters the basement at instruction {}'.format(count)
            entered_basement = True
        count +=1
print 'He needs to end up at floor {}'.format(floor)
