# Day 2
# Part 1: input is a list of passports separated by blank lines
# Passports contain:
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
#
# Count how many passports are valid, they must contain every item except cid which is optional
#
# Part 2: add some validation to the mandatory fields!
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
#     If cm, the number must be at least 150 and at most 193.
#     If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
#
# After looking through some other answers, ways to improve code are:
#     read in passports using passports = [chunk.split() for chunk in open("input.txt").read().split("\n\n")]
#     then data = dict(line.split(':')  for line in passport)
#     can also use lambda functions instead of always regex -> should be more efficient for the date-type checks
#     e.g. REQUIRED_FIELDS = {"byr": lambda s: 1920 <=int(s) <= 2002, # Birth Year....
#     for field, func in REQUIRED_FIELDS.items():
#     if not func(data[field]):

import re
current_passport = {}
passports = []
for line in open('input_04.txt'):
    if line == '\n':
        passports.append(current_passport.copy())
        current_passport = {}
    else:
        for chunk in line.strip('\n').split():
            key_value = chunk.split(':')
            current_passport[key_value[0]] = key_value[1]

passports.append(current_passport)

categories = {'byr':'19[2-9][0-9]|200[0-2]'
              ,'iyr':'201[0-9]|2020'
              ,'eyr':'202[0-9]|2030'
              ,'hgt':'1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in'
              ,'hcl':'^#[0-9a-f]{6}$'
              ,'ecl':'amb|blu|brn|gry|grn|hzl|oth'
              ,'pid':'^\d{9}$'}
part1, part2 = 0, 0
for passport in passports:
    p1, p2 = True, True
    for key in categories:
        if key not in passport:
            p1, p2 = False, False
            break
        elif not re.search(categories[key],passport[key]):
            p2 = False
    if p1 == True:
        part1 +=1
        if p2 == True:
            part2 +=1

print('Part 1: {}, Part 2: {}'.format(part1,part2))
