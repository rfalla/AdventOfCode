# Day 20
# infinite elves delivering presents to infinite houses
# each elf delivers presents to houses that are multiples of it's number
# each elf delivers 10* it's number
# elves and houses are numbered from 1 -> inf
# what is the first house to recieve > 36000000 presents

# This method is exceedingly slow
# but it does work
def factors(n):
    return set(x for tup in ([i, n//i] 
                for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)

if __name__ == "__main__":

    h = 10000
    presents = 0
    over50 = {}
    while presents < 36000000:
        presents = 0
        factors_list = factors(h)
        for p in factors_list:
            # part 1
            # presents += 10*p
            # part 2
            if p not in over50:
                presents += 11*p
                over50[p] = 1
            elif over50[p] < 50:
                presents += 11*p
                over50[p] += 1
            else:
                continue
        h += 1
    
    print h-1
