# Puzzle input is a list of foods.
# Each line is a list of ingredients.
# Each ingredient contains 0 or 1 allergens and each allergen is found in one ingredient.
# Part 1: Work out which ingredients do not contain any allergens and count the number of times they show up.
# Part 2: Work out the ingredient-allergen pairings and create a "canonical dangerous list" by arranging the ingredients alphabetically by their allergen and separate them by commas.
from collections import defaultdict
input = [x.strip('\n').split(' (contains ') for x in open('input_21.txt')]
possible_pairs = defaultdict(set)
all_ingredients = []
all_allergens = set()
for line in input:
    ingredients = set(line[0].split())
    allergens = line[1][:-1].replace(',','').split()
    all_ingredients+= ingredients
    all_allergens.update(allergens)
    for a in allergens:
        if len(possible_pairs[a]) == 0:
            possible_pairs[a] = ingredients
        else:
            possible_pairs[a] = possible_pairs[a].intersection(ingredients)

set_allergens = {}
while True:
    if len(all_allergens) == len(set_allergens):
        break
    for key1, value1 in possible_pairs.items():
        if len(value1) > 1:
            continue
        if key1 in set_allergens:
            continue
        v,=value1
        set_allergens[key1] = v
        for key2, value2 in possible_pairs.items():
            if key1 != key2:
                possible_pairs[key2] = value2.difference(value1)
    
part1 = sum([1 for x in all_ingredients if x not in set_allergens.values()])
part2 = ','.join([value for key, value in sorted(set_allergens.items())])
print('Part 1: {}, Part 2: {}'.format(part1, part2))
