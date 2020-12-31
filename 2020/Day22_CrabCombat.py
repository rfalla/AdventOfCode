# 2 Player card game.
# Part 1: Combat.
# Each player takes out their top card, whoever has highest wins the round and places both cards to the bottom of their pile.
# The winner is the person with all of the cards at the end.
# The winning players score is equal to the sum of the value of each card * its inverse place in the deck (e.g. last =1, 10th from last = 10).
# What is the winning players score?
#
# Part 2: Recursive Combat.
# Extra rules:
#    Before you play a round, if there was a previous round with the same card orders for the same players then the game immediately ends and Player 1 wins.
#    If both players have at least as many cards remaining in their deck as the value of the card they just drew, the winner of the round is determined by playing a new game of Recursive Combat.
#    Otherwise, at least one player must not have enough cards left in their deck to recurse; the winner of the round is the player with the higher-value card.
# To play a sub-game of Recursive Combat, each player creates a new deck by making a copy of the next cards in their deck.
# The quantity of cards copied is equal to the number on the card they drew to trigger the sub-game.
#
# Probably a bit overkill using dictionaries for the players - I was anticipating part 2 including more players. If I were to redo this I would likely just have 2 lists or even deques and not have to do so much comprehension.
# Also found out that the sub-games can be optimised if P1 has the max card.
from collections import deque
from copy import deepcopy
from itertools import islice
def parse(filename):
    players_raw = [x.strip('\n').split('\n') for x in open(filename).read().split("\n\n")]
    cards = {}
    for player in players_raw:
        id = int(player[0][7:-1])
        cards[id] = deque([int(x) for x in player[1:]])
    return cards

def calculate_winning_score(cards, winner):
    winning_cards = cards[winner]
    return sum([(len(winning_cards)-i)*v for i,v in enumerate(winning_cards)])

def combat(cards):
    while True:
        if any([len(x) == 0 for x in cards.values()]):
            break
        top_cards = {key: value.popleft() for key, value in cards.items()}
        cards[max(top_cards, key=top_cards.get)].extend(sorted(top_cards.values(), reverse=True))
    winner = [i for i,v in cards_part1.items() if len(v) > 0][0]
    score =  calculate_winning_score(cards, winner)
    print('Player {} is the winner of Combat! They have a score of {}'.format(winner, score))
    return None

def recursive_combat(cards, game_number = 1):
    card_cache = set()
    #print('New game! '+str(game_number))
    while True:
        #print(cards[1],cards[2])
        # Check if any deques are empty
        if any([len(x) == 0 for x in cards.values()]):
            #print('A player is out of cards.')
            break
        # Check for previous rounds
        cache_key = (tuple(cards[1]), tuple(cards[2]))
        if cache_key in card_cache:
            #print('Infinite loop - player 1 wins!')
            if game_number == 1:
                score =  calculate_winning_score(cards,1)
                #print('Player 1 is the winner of Recursive Combat! They have a score of {}'.format(score))
            return 1
        # Add current cards to cache
        card_cache.add(cache_key)
        # Pick top cards
        top_cards = {key: value.popleft() for key, value in cards.items()}
        if any([len(cards[key]) < value for key, value in top_cards.items()]):
            # If either hand has top card > len(cards left) then highest card wins
            cards[max(top_cards, key=top_cards.get)].extend(sorted(top_cards.values(), reverse=True))
        else:
            # Otherwise play recursively
            # It seems that the usefullness of deque has run out here - cannot slice it!
            winner = recursive_combat({key: deque(islice(cards[key],0,value)) for key, value in top_cards.items()}, game_number+1)
            #print('back in game '+ str(game_number))
            cards[winner].append(top_cards[winner])
            cards[winner].append(top_cards[[x for x in top_cards.keys() if x != winner][0]])

    winner = [i for i,v in cards.items() if len(v) > 0][0]
    if game_number == 1:
        score =  calculate_winning_score(cards, winner)
        print('Player {} is the winner of Recursive Combat! They have a score of {}'.format(winner, score))
    return winner

if __name__=="__main__":
    cards = parse('input_22.txt')
    cards_part1 = deepcopy(cards)
    combat(cards_part1)
    recursive_combat(cards)
