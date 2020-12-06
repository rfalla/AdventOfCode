def FuelCalc(x):
    y = max(x/3-2,0)
    return y

def FuelForFuel(FuelList):
    return [FuelCalc(x) for x in FuelList if FuelCalc(x) > 0]

# Part 1, for sum floor(X/3) -2 for each value in
# Part 2, same as Part 1 except for each value, we keep applying the equation until we hit 0 or less.
list1 = [FuelCalc(int(line.rstrip('\n'))) for line in open('input_01.txt')]
total = 0

def RecursiveFuelForFuel(FuelList):
    global total
    total += sum(FuelList)
    if len(FuelList) == 0:
        return 0
    else:
        return RecursiveFuelForFuel(FuelForFuel(FuelList))

RecursiveFuelForFuel(list1)
print(total)


