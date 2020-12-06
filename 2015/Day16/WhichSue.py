# Day 16
# recieved present from Aunt Sue
# have 500 Aunt Sues
# present tells you some properties of the giver
# have a list of things you remember about your Aunts
# work out which Aunt gave gift
#
# properties include:
# children, cats, samoyeds, pomeranians, akitas, vizslas, goldfish, trees, cars, perfumes
# if a property is not set then the value is unknown (!= 0) so assign it -1
#
# giver has properties:
# children: 3
# cats: 7
# samoyeds: 2
# pomeranians: 3
# akitas: 0
# vizslas: 0
# goldfish: 5
# trees: 3
# cars: 2
# perfumes: 1

auntmap = {}
auntmap['children'] = 3
auntmap['cats'] = 7
auntmap['samoyeds'] = 2
auntmap['pomeranians'] = 3
auntmap['akitas'] = 0
auntmap['vizslas'] = 0
auntmap['goldfish'] = 5
auntmap['trees'] = 3
auntmap['cars'] = 2
auntmap['perfumes'] = 1


input = open('input.txt')
for line in input:
    line_1 = line.replace(':','')
    line_2 = line_1.replace(',','')
    words = line_2.split(' ')
    isGiver = True
    for i in range(2,len(words)-1,2):
        # Part 1
        #if auntmap[words[i]] != int(words[i+1]):
        #    isGiver = False
        #    continue
        # Part 2
        if words[i] == 'cats' or words[i] == 'trees':
            if auntmap[words[i]] >= int(words[i+1]):
                isGiver = False
                continue
        elif words[i] == 'pomeranians' or words[i] == 'goldfish':
            if auntmap[words[i]] <= int(words[i+1]):
                isGiver = False
                continue
        else:
            if auntmap[words[i]] != int(words[i+1]):
                isGiver = False
                continue
    if isGiver == True:
        print words[1]

