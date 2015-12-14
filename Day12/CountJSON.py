# Day 12
# input is file containing JSON
# count all numbers in it
################################

floors = open('input.txt')
count = 0
for word in floors:
    nChar = len(word)
    ch = 0
    while ch < nChar:
        if ch+1 >= nChar and word[ch].isdigit():
            count += int(word[ch])
            ch += 1
        if word[ch].isdigit() and not word[ch+1].isdigit():
            if ch == 0:
                count += int(word[ch])
            elif word[ch-1] == "-":
                count -= int(word[ch])
            else:
                count += int(word[ch])
            ch += 1
        elif word[ch].isdigit() and word[ch+1].isdigit():
            num = int(word[ch])
            neg = False
            if word[ch-1] == "-":
                neg = True
            i = 1
            while ch+i < nChar and word[ch+i].isdigit():
                num *= 10
                num += int(word[ch+i])
                i += 1
            ch += i+1
            if neg:
                count -= num
            else:
                count += num
        else:
            ch += 1
            

print 'Total = {}'.format(count)
