with open('input.txt') as f:
    content = f.readlines()
    f.close
content = [x.strip() for x in content]

level = 1
score = 0
for ch in content[0]:
    if ch == '{':
        score += level
        level += 1
    elif ch == '}':
        level -= 1
#    print(ch, score, level)
#print(score)

garbage = 0
inGarbage = False
for ch in content[0]:
    if inGarbage == True and ch != '>':
        garbage += 1
    if ch == '<':
        inGarbage = True
    elif ch == '>':
        inGarbage = False
print(garbage)
