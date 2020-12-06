from itertools import combinations
input = [1,2,3,5,7,13,17,19,23,29,31,37,41,43,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113]
total = sum(input)
total /= 4#3
minQE = 100000000000000000000
# worked out these values in my head - P1 min number of packages = 6, P2 = 4
for comb in combinations(input,4):
    if sum(list(comb)) == total:
        print list(comb)
        input_left = [x for x in input if x not in list(comb)]
        i = 4#6
        works = False
        while i < (len(input) - 7) and works == False: #11
            for comb2 in combinations(input_left,i):
                if sum(list(comb2)) == total:
                    ## remove for part 1 ##
                    input_left2 = [x for x in input if x not in list(comb2)]
                    j = 4
                    while j < (len(input) - 7 - j) and works == False:
                        for comb3 in combinations(input_left2,j):
                            if sum(list(comb3)) == total:
                                works = True
                    ####
                    #works = True
            i += 1
        if works == True:
            QE = reduce(lambda x, y: x*y, list(comb))
            if QE < minQE:
                minQE = QE
print minQE
        


