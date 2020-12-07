# Part 1: We are given rules about what bags can contin bags e.g.
# light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.
#
# How many bags can contain a shiny gold bag?
#
# Part 2: How many bags are within 1 shiny gold bag?
import re
shiny_gold = 'shiny gold'
bags = {}

regex_parent = re.compile('([a-z][a-z\s]+)\sbags\scontain\s(.+)')
regex_children = re.compile('(\d+)\s([a-z\s]+)\sbag')

parents = [re.match(regex_parent, x.strip('\n')).groups() for x in open('input_07.txt')]
for parent, children in parents:
    if parent not in bags:
        bags[parent] = {}
    for num, child in re.findall(regex_children,children):
        bags[parent][child] = num

def count_bags_containing_target(bags, target, contains_target = set()):
    for key, value in bags.items():
        if target in value and key not in contains_target:
            contains_target.add(key)
            count_bags_containing_target(bags, key, contains_target)
    return len(contains_target)

def target_counter(bags, target):
    counter=1
    for key, value in bags[target].items():
        counter += int(value) * target_counter(bags, key)
    return counter

print('Part 1: {}, Part 2: {}'.format(count_bags_containing_target(bags, shiny_gold), target_counter(bags, shiny_gold)-1))
