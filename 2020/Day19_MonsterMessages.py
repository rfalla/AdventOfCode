# Input is a list of rules and messages. Rules either list a single value, or a list of rules that must be followed in order, the "|" means OR:
# 0: 1 2
# 1: "a"
# 2: 1 3 | 3 1
# 3: "b"
# Part 1: how many messages completely match rule 0?
# Initially started building up the rules using recursion and regex, but it got quite tricky when replacing values.
# After help from r/AoC re-implemented instead by checking through each string char-by-char.
# Part 2: replace rules 8: 42 and 11: 42 31 with the following:
#    8: 42 | 42 8
#    11: 42 31 | 42 11 31
# Now there is an infinite number of message solutions! Luckily I changed tactics for part 1 otherwise I would have had to refactor my code anyway.
def check_rules(rules, message, target):
    #Check if we have reached the end of either the input message or the rules. This captures different length strings.
    if message == '' or target == []:
        return message == '' and target == []

    #print('Checking message {} against target {}'.format(message, target[0]))
    rule = rules[target[0]]
    if 'a' in rule[0] or 'b' in rule[0]:
        if rule[0] == message[0]:
            #print('a or b in rule and match, {}, {}'.format(rule, message))
            return check_rules(rules, message[1:], target[1:])
        else:
            #print('a or b in rule and don\'t match, {}, {}'.format(rule, message))
            return False
    else:
        #print('Going into ANY function with remainder of target')
        return any(check_rules(rules, message, r + target[1:]) for r in rule)
                               

if __name__=="__main__":
    input = [x.replace('"','').split('\n') for x in open("input_19.txt").read().split("\n\n")]
    rules = {}
    for line in input[0]:
        key, value = line.split(': ')
        if not value[0] in ['a','b']:
            value = [[int(x) for x in y.split()] for y in value.split('|')]
        rules[int(key)] = value
    messages = input[1][0:-1]
    part1 = sum([check_rules(rules, m, [0]) for m in messages])
    rules[8] =[[42], [42, 8]]
    rules[11] = [[42, 31],  [42, 11, 31]]
    part2 = sum([check_rules(rules, m, [0]) for m in messages])
    print('Part 1: {}, Part 2: {}'.format(part1, part2))
