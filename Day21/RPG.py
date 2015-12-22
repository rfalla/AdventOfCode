# Day 21
# You are playing an RPG
# You go first, boss goes next...etc take it in turns
# damage_dealt = max(1, damage_attacker - armour_attackee) 
# have infinite gold to buy stuff from inventory
# shopping limitations:
## nWeapons == 1
## nArmour <= 1
## nRings <= 2
## can only buy each item once
# You start with 100hp
# Your boss has 109hp, 8d,2a
# find the min amount of gold you can soend and still win
from itertools import combinations

def fight(me):
    meHP = me['hp']
    boHP = boss['hp']
    while meHP > 0 and boHP > 0:
        boHP -= max(1,me['damage']-boss['armor'])
        meHP -= max(1,boss['damage']-me['armor'])
    if meHP <= 0:
        return False
    elif boHP <= 0:
        return True

def stats(list,meHP):
    hps = ['cost','damage','armor']
    for hp in hps:
        tally = 0
        for item in list:
            tally += inventory[item,hp]
        meHP[hp] = tally
    return meHP

if __name__ == "__main__":
    global boss
    boss = {}
    boss['hp'] = 109
    boss['damage'] = 8
    boss['armor'] = 2
    weapons = []
    armor = []
    rings = []
    global inventory
    inventory = {}
    input = open('input.txt')
    i = 0
    for line in input:
        words = line.split()
        if i > 0 and i < 6:
            if words[0] not in weapons:
                weapons.append(words[0])
            inventory[words[0],'cost'] = int(words[1])
            inventory[words[0],'damage'] = int(words[2])
            inventory[words[0],'armor'] = int(words[3])
        if i > 7 and i < 13:
            if words[0] not in armor:
                armor.append(words[0])
            inventory[words[0],'cost'] = int(words[1])
            inventory[words[0],'damage'] = int(words[2])
            inventory[words[0],'armor'] = int(words[3])
        if i > 14 and i < 21:
            if words[0] not in rings:
                rings.append(words[0]+str(i))
            inventory[words[0]+str(i),'cost'] = int(words[2])
            inventory[words[0]+str(i),'damage'] = int(words[3])
            inventory[words[0]+str(i),'armor'] = int(words[4])
        i += 1

    costWin = 10000000000
    costLose = 0
    choice = []
    for weapon in weapons:
        me = {}
        me['hp'] = 100
        a = 0
        while a < 2:
            for armor_com in combinations(armor,a):
                r = 0
                while r < 3:
                    for rings_com in combinations(rings,r):
                            testlist = []
                            testlist.append(weapon)
                            for armo in armor_com:
                                testlist.append(armo)
                            for ring in rings_com:
                                testlist.append(ring)
                            me = stats(testlist,me)
                            doWin = fight(me)
                            if doWin == True and me['cost'] < costWin:
                                costWin = me['cost']
                                choice = testlist
                            if doWin == False and me['cost'] > costLose:
                                costLose = me['cost']
                    r += 1
            a += 1

    print costWin,costLose
