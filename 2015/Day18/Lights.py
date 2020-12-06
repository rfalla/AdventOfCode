# Day 18
# Santa gives you a lighting plan for a 100x100 grid
# "#" means on
# "." means off
# succesive steps are taken by counting the number of on lights around a light
# For on lights: stay on if 2 or 3 neighbours are lit; off otherwise
# For off lights: turn on if 3 neighbours are on; off otherwise
# update happens simultaneously
# find out how many lights are on after 100 iterations
# Part 2, the four corners are always on, repeat

def turnOn(plan,x,y):
    count = 0
    if x+1 < 100 and plan[x+1][y] == '#':
        count += 1
    if x+1 < 100 and y+1 < 100 and plan[x+1][y+1] == '#':
        count += 1
    if x+1 < 100 and y-1 > -1 and plan[x+1][y-1] == '#':
        count += 1
    if y+1 < 100 and plan[x][y+1] == '#':
        count += 1
    if y-1 > -1 and plan[x][y-1] == '#':
        count += 1
    if x-1 > -1 and plan[x-1][y] == '#':
        count += 1
    if x-1 > -1 and y+1 < 100 and plan[x-1][y+1] == '#':
        count += 1
    if x-1 > -1 and y-1 > -1 and plan[x-1][y-1] == '#':
        count += 1

    if plan[x][y] == '#' and (count == 2 or count == 3):
        return True
    if plan[x][y] == '.' and (count == 3):
        return True
    else:
        return False

if __name__ == "__main__":
    input = open('input.txt')
    x = 0
    plan = [['' for j in range(100)] for i in range(100)]
    for line in input:
        for y in range(0,100):
            plan[x][y] = line[y]
        x+=1
    plan[0][0] = '#'
    plan[0][99] = '#'
    plan[99][0] = '#'
    plan[99][99] = '#'

    iter = 0
    while iter < 100:
        nextPlan = [['.' for j in range(100)] for i in range(100)]
        for i in range(100):
            for j in range(100):
                if turnOn(plan,i,j) == True:
                    nextPlan[i][j] = '#'
        nextPlan[0][0] = '#'
        nextPlan[0][99] = '#'
        nextPlan[99][0] = '#'
        nextPlan[99][99] = '#'
        plan = nextPlan
        iter += 1
    
    total = 0
    for j in range(100):
        for k in range(100):
            if plan[j][k] == '#':
                total += 1
    print total
