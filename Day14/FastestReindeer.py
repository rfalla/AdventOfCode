# Day 14
# Simple whose the fastest reindeer after 2503 seconds
# each reindeer has a speed, how long it can fly at that speed
# and how long it needs to rest before taking off again

def find_dist(rd,time):
    fly_full = rd[1]
    fly_full *= (time/(rd[1]+rd[2]))
    fly_part = min(time%(rd[1]+rd[2]),rd[1])
    fly = fly_full + fly_part
    return fly*rd[0]

def find_fastest(reindeer,time):
    max = 0
    names = {}
    for rd in reindeer:
        if find_dist(reindeer[rd],time) >= max:
            max = find_dist(reindeer[rd],time)
            names[rd] = max
        for r in list(names):
            if names[r] < max:
                del names[r]
    return names

def find_most_points(reindeer,time):
    points = {}
    for t in range(1,time+1):
        rd = find_fastest(reindeer,t)
        for r in rd:
            if r in points:
                points[r] += 1
            else:
                points[r] = 1
    max = 0
    mp = ''
    for rd in points:
        if points[rd] >= max:
           mp = rd
           max = points[rd]
    print 'The reindeer with the most points is {0} with {1} points'.format(mp,max)

if __name__ == "__main__":
    reindeer = {}
    input = open('input.txt')
    for line in input:
        words = line.split(' ')
        reindeer[words[0]] = [int(words[3]),int(words[6]),int(words[13])]
    fastest = find_fastest(reindeer,2503)
    for i in fastest:
        print 'The fastest reindeer at {0}s is {1}, with {2}km.'.format(2503,i,fastest[i])
    find_most_points(reindeer,2503)
