# Day 10
# given int
# use look-and-see to find next int
# e.g. 1->11->21->1211->111221->....
# find length of int after 40/50 iterations (Part1/Part2)
# starter input = 1113222113

# This code is quite slow, would need optimising for use in real world
def FindNext(current):
    i = 0
    next = []
    while i < len(current):
        n = 1
        keepLooking = True
        while keepLooking == True:
            if i+n >= (len(current) - 1):
                keepLooking = False
            elif current[i+n] == current[i]:
                n += 1
            else:
                keepLooking = False
        next.append(n)
        next.append(current[i])
        i += n
    return next

if __name__ == "__main__":
    input = [1,1,1,3,2,2,2,1,1,3]
    i = 0
    while i < 50:
        input = FindNext(input)
        i+=1

    print len(input)
