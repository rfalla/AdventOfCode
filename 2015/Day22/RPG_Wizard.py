# Day 22
# You are playing an RPG
# You go first, boss goes next...etc take it in turns
# This time you use spells instead of stuff
# mana = gold
# spells can last for more than one turn (effect)
import random

def checkEffects():
    # Part 2 #
    #me['hp'] -= 1
    #--------#
    if effects['missile'] > 0:
        if (debug):
            print 'Missile deals 4 damage, {} turns left on timer'.format(effects['missile']-1)
        boss['hp'] -= 4
        effects['missile'] -= 1
    if effects['drain'] > 0:
        if (debug): 
            print 'Drain deals 2 damage and gives 2hp, {} turns left on timer'.format(effects['drain']-1)
        boss['hp'] -= 2
        me['hp'] += 2
        effects['drain'] -= 1
    if effects['shield'] > 0:
        if (debug):
            print 'Shield is on, {} turns left on timer'.format(effects['shield']-1)
        me['armor'] = 7
        effects['shield'] -= 1
        if effects['shield'] == 0:
            me['armor'] = 0
    if effects['poison'] > 0:
        if (debug):
            print 'Poison deals 3 damage, {} turns left on timer'.format(effects['poison']-1)
        boss['hp'] -= 3
        effects['poison'] -= 1
    if effects['recharge'] > 0:
        if (debug):
            print 'Recharge gives 101 mana, {} turns left on timer'.format(effects['recharge']-1)
        me['mana'] += 101
        effects['recharge'] -= 1
        
def bossTurn():
    damage = max(1,boss['damage']-me['armor'])
    if (debug):
        print 'Boss attacks {} damage'.format(damage)
    me['hp'] -= damage
    return 1

def meTurn(spell):
    if (debug):
        print 'Player casts {0}, cost = {1}, total cost = {2}'.format(spell,spells[spell,'mana'],cost)
    me['mana'] -= spells[spell,'mana']
    effects[spell] = spells[spell,'effect']
    return 1

if __name__ == "__main__":
    # setup
    global debug
    debug = True
    global spells
    spells = {}
    spells['missile','mana'] = 53
    spells['missile','effect'] = 1
    spells['drain','mana'] = 73
    spells['drain','effect'] = 1
    spells['shield','mana'] = 113
    spells['shield','effect'] = 6
    spells['poison','mana'] = 173
    spells['poison','effect'] = 6
    spells['recharge','mana'] = 229
    spells['recharge','effect'] = 5
    spells_list = ['missile','drain','shield','poison','recharge']
    # actual play
    global cost
    global boss
    boss = {}
    global me
    me = {}
    global effects
    effects = {}
    minCost = 1000000000
    # going to choose spells randomly and hopefully after 100,000 goes it will have found the cheapest way!
#    i = 0
#    notWon = True
#    while i < 10000000:#notWon == True:#i < 10000000:
    boss['hp'] = 71
    boss['damage'] = 10
    me['hp'] = 50
    me['mana'] = 500
    me['armor'] = 0
    effects['missile'] = 0
    effects['drain'] = 0
    effects['shield'] = 0
    effects['poison'] = 0
    effects['recharge'] = 0
    cost = 0
    list = ['recharge','shield','missile','poison','recharge','shield','missile','poison','recharge','shield','missile','poison','missile','missile']
    while boss['hp'] > 0 and me['hp'] > 0 and cost < minCost:
        for i in range(14):
            if (debug):
                print '-- Player Turn --'
                print '- Player has {0} hp, {1} armor, {2} mana'.format(me['hp'],me['armor'],me['mana'])
                print '- Boss has {} hp'.format(boss['hp'])
            checkEffects()
            if boss['hp'] <= 0 or me['hp'] <= 0 or me['mana'] < 53:
                break
            #canUse = False
            #spell = 'missile'
            #while canUse == False:
            #    spell = random.choice(spells_list)
            #    if me['mana'] >= spells[spell,'mana'] and effects[spell] < 1:
            #        canUse = True
            spell = list[i]
            cost += spells[spell,'mana']
            meTurn(spell)
            if boss['hp'] <= 0 or me['hp'] <= 0 or me['mana'] < 53:
                break
            if (debug):
                print '-- Boss Turn --'
                print '- Player has {0} hp, {1} armor, {2} mana'.format(me['hp'],me['armor'],me['mana'])
                print '- Boss has {} hp'.format(boss['hp'])
            checkEffects()
            if boss['hp'] <= 0 or me['hp'] <= 0:
                break
            bossTurn()
            if boss['hp'] <= 0 or me['hp'] <= 0 or me['mana'] < 53:
                break
        if (debug):
            if me['mana'] < 53:
                print '-- not enough mana --'
            elif cost >= minCost:
                print '-- costs too much --'
            elif boss['hp'] <= 0 and me['hp'] > 0:
                print '-- Player Wins --'
                print '... at a price of {} mana\n\n'.format(cost)
                if cost < minCost:
                    minCost = cost
                    notWon = False
            else:
                print '-- Boss Wins --\n\n'
        else:
            if me['hp'] > 0 and boss['hp'] <= 0 and cost < minCost:
                minCost = cost
                notWon = False
        #i += 1

    print 'minimum cost was {}'.format(minCost)
