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
        if entered_basement == False and floor == -1:
            print 'He first enters the basement at instruction {}'.format(count)
            entered_basement = True
        count +=1
print 'He needs to end up at floor {}'.format(floor)
