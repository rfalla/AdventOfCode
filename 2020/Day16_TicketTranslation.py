# Input is a set of three lists: first is a set of rules for categories, second is my ticket, 3rd is other tickets.
# Tickets are csvs with categories in same order, but we don't know the order.
# Part 1: sum the invalid numbers in the other tickets.
# Part 2: discard the invalid tickets. From the remaing tickets determine the category order.
# Return the multiplication of the values of catgories starting 'departure' in my ticket.
#
# I HATE this code, way too many nested loops, quite messy.
import re
from functools import reduce

def parse(filename):
    file = open(filename,'r')
    rules ={}
    blank_count = 0
    other_tickets = []
    for line in file.readlines():
        if line == '\n':
            blank_count+=1
        if blank_count < 1:
            rule = re.match('([a-z\s]+):\s([\d]+)-([\d]+)\sor\s([\d]+)-([\d]+)', line.strip('\n')).groups()
            rules[rule[0]] = [int(x) for x in rule[1:]]
        elif blank_count == 1:
            if line[0].isdigit():
                my_ticket = [int(x) for x in line.strip('\n').split(',')]
        elif line[0].isdigit():
            other_tickets.append([int(x) for x in line.strip('\n').split(',')])
    file.close()
    return rules, my_ticket, other_tickets

def find_valid_numbers(rules):
    # This will probably only get used in part 1
    valid_numbers = []
    for r in rules:
        for i in range(rules[r][0], rules[r][1]+1):
            valid_numbers.append(i)
        for i in range(rules[r][2], rules[r][3]+1):
            valid_numbers.append(i)
    return set(valid_numbers)

def sum_error_rate(other_tickets, valid_numbers):
    error_rate = 0
    valid_tickets = []
    for ticket in other_tickets:
        err = sum([x for x in ticket if x not in valid_numbers])
        if err == 0:
            valid_tickets.append(ticket)
        error_rate += err
    return error_rate, valid_tickets

def check_rule(rule, n):
    return (rule[0] <= n <= rule[1]) or (rule[2] <= n <= rule[3])

def find_category_order(rules, valid_tickets):
    # Transposing the data
    columns = {}
    potential_rules = {}
    potential_columns = {}
    for i in range(len(rules)):
        columns[i] = [x[i] for x in valid_tickets]
        potential_rules[i] = list(rules.keys())
        potential_columns[list(rules.keys())[i]] = list(range(len(rules)))
    settled_rules = {}
    for column in columns:
        for c in columns[column]:
            for rule in potential_rules[column]:
                if check_rule(rules[rule],c) == False:
                    potential_rules[column].remove(rule)
                    potential_columns[rule].remove(column)
                    break
    cols_to_remove = []
    
    while True:
        for col in potential_rules:
            potential_rules[col] = [x for x in potential_rules[col] if x not in cols_to_remove]
            if len(potential_rules[col]) == 1:
                settled_rules[potential_rules[col][0]] = col
                if col not in cols_to_remove: cols_to_remove.append(col)
        for rule in potential_columns:
            if len(potential_columns[rule]) == 1:
                settled_rules[rule] = potential_columns[rule][0]
                potential_rules.pop(potential_columns[rule][0], None)
                if potential_columns[rule][0] not in cols_to_remove: cols_to_remove.append(potential_columns[rule][0])
        for rule in settled_rules:
            [potential_rules[x].remove(rule) for x in potential_rules if rule in potential_rules[x]]

        if len(settled_rules) == len(rules):
            break
    return settled_rules

if __name__=="__main__":
    rules, my_ticket, other_tickets = parse('input_16.txt')
    valid_numbers = find_valid_numbers(rules)
    error_rate, valid_tickets = sum_error_rate(other_tickets, valid_numbers)
    valid_tickets.append(my_ticket)
    category_order = find_category_order(rules, valid_tickets)
    part2 =reduce((lambda a, b: a*b), ([my_ticket[category_order[x]] for x in category_order.keys() if x.startswith('departure')]))
    print('Part 1: {}, Part 2: {}'.format(error_rate, part2))
