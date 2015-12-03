instructions = open('elfInstructions.txt')
currentHouse = [0,0]
houses = {}
houses[(0,0)] = 1
for word in instructions:
    for ch in word:
        if ch == '^':
            currentHouse[0]+=1
        elif ch == 'v':
            currentHouse[0]-=1
        elif ch == '<':
            currentHouse[1]-=1
        elif ch == '>':
            currentHouse[1]+=1
        if (currentHouse[0],currentHouse[1]) in houses:
            houses[(currentHouse[0],currentHouse[1])]+=1
        else:
            houses[(currentHouse[0],currentHouse[1])] = 1
print len(houses)
