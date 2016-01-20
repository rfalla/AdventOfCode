# Day 22
# You are playing an RPG
# You go first, boss goes next...etc take it in turns
# This time you use spells instead of stuff
# mana = gold
# spells can last for more than one turn (effect)

def takeTurn(spell, boss_hp, boss_damage, me_hp, me_mana, _cost, _shield, _poison, _recharge):
    #print spell, _cost, _shield, _poison, _recharge
    global minCost
    if (debug):
        print '-- Player Turn --'
        print '- Player has {0} hp, {1} mana'.format(me_hp,me_mana)
        print '- Boss has {} hp'.format(boss_hp)
        print '- cost so far is {}'.format(_cost)
    armor = 0
    # Part 2 #
    if (part2):    
        me_hp -= 1
    #--------#
    if _shield > 0:
        if (debug):
            print 'Shield is on, player armor = 7, {} turns left on timer'.format(_shield-1)
        armor = 7
        _shield -= 1
    if _poison > 0:
        if (debug):
            print 'Poison deals 3 damage, {} turns left on timer'.format(_poison-1)
        boss_hp -= 3
        _poison -= 1
    if _recharge > 0:
        if (debug):
            print 'Recharge gives 101 mana, {} turns left on timer'.format(_recharge-1)
        me_mana += 101
        _recharge -= 1

    if boss_hp <= 0 and me_hp > 0:
        if (debug):
            print 'Player Wins! At a cost of {}'.format(_cost)
        if _cost < minCost:
            if (debug):
                print 'This is a new minimum cost'
            minCost = _cost
            return True

    if (debug):
        print 'Player uses {}'.format(spell)
    if spell == 'missile':
        boss_hp -= 4
    elif spell == 'drain':
        boss_hp -= 2
        me_hp += 2
    elif spell == 'shield':
        if _shield == 0:
            _shield = 6
        else:
            if (debug):
                print 'shield already in play'
            return False
    elif spell == 'poison':
        if _poison == 0:
            _poison = 6
        else:
            if (debug):
                print 'poison already in play'
            return False
    elif spell == 'recharge':
        if _recharge == 0:
            _recharge = 5
        else:
            if (debug):
                'recharge already in play'
            return False

    me_mana -= spellcost[spell]
    _cost += spellcost[spell]

    if _cost > minCost:
        if (debug):
            print 'current cost > {}'.format(minCost)
        return False

    if boss_hp <= 0 and me_hp > 0:
        if (debug):
            print 'Player Wins! At a cost of {}'.format(_cost)
        if _cost < minCost:
            if (debug):
                print 'This is a new minimum cost'
            minCost = _cost
            return True

    if (debug):
        print '-- Boss Turn --'
        print '- Player has {0} hp, {1} mana'.format(me_hp,me_mana)
        print '- Boss has {} hp'.format(boss_hp)

    armor = 0
    if _shield > 0:
        if (debug):
            print 'Shield is on, player armor = 7, {} turns left on timer'.format(_shield-1)
        armor = 7
        _shield -= 1
    if _poison > 0:
        if (debug):
            print 'Poison deals 3 damage, {} turns left on timer'.format(_poison-1)
        boss_hp -= 3
        _poison -= 1
    if _recharge > 0:
        if (debug):
            print 'Recharge gives 101 mana, {} turns left on timer'.format(_recharge-1)
        me_mana += 101
        _recharge -= 1

    if boss_hp <= 0 and me_hp > 0:
        if (debug):
            print 'Player Wins! At a cost of {}'.format(_cost)
        if _cost < minCost:
            if (debug):
                print 'This is a new minimum cost'
            minCost = _cost
            return True

    me_hp -= max((boss_damage - armor),1)
    if me_hp <= 0:
        if (debug):
            print 'Boss Wins!'
        return False

    for nextspell in spells_list:
        if me_mana > spellcost[nextspell]:
            takeTurn(nextspell, boss_hp, boss_damage, me_hp, me_mana, _cost, _shield, _poison, _recharge)
    if (debug):
        print 'Boss Wins!'
    return False

if __name__ == "__main__":
    # setup
    global debug
    debug = True
    global part2
    part2 = True
    global spells_list
    spells_list = ['missile','drain','shield','poison','recharge']
    global spellcost
    spellcost = {}
    spellcost['missile'] = 53
    spellcost['drain'] = 73
    spellcost['shield'] = 113
    spellcost['poison'] = 173
    spellcost['recharge'] = 229
    global minCost
    minCost = 3000 # I know from previous code that both answers are < 3000
    for spell in spells_list:
        takeTurn(spell, 71, 10, 50, 500, 0, 0, 0, 0)
    print 'minimum cost was {}'.format(minCost)
