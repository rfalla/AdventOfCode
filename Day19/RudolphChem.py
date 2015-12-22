# Day 19
# need to make Rudolph some medicine
# Part 1: calibration
# given mol, how many different molecules can this be converted to
# using the conversions in input.txt
# only convert one at a time
# Part 2: starting from e, what is the fewest number of steps taken to get to mol
from random import shuffle

mol = 'ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF'

input = open('input.txt')
fromlist = []
tolist = []
conversions = []
for line in input:
    words = line.split(' => ')
    fromlist.append(words[0])
    tolist.append(words[1].replace('\r\n',''))
    conversions.append((words[0],words[1].replace('\r\n','')))

changes = []
for i in range(len(fromlist)):
    search = mol.find(fromlist[i])
    l = len(fromlist[i])
    while search > -1:
        newString = mol[:search]+tolist[i]+mol[search+l:]
        if newString not in changes:
            changes.append(newString)
        search = mol.find(fromlist[i],search+1)
print len(changes)

# attempt at Part 2
# couldn't think of a better way to do this without cutting into
# xmas celebrations
# so i've gone for the random approach

target = mol
steps = 0
while target != 'e':
    tmp = target
    for a, b in conversions:
        if b not in target:
            continue

        target = target.replace(b, a, 1)
        steps += 1

    if tmp == target:
        target = mol
        steps = 0
        shuffle(conversions)

print steps


