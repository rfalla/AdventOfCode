# Day 4
# given the key 'yzbqklnj'
# find the lowest positive number that when appended to the key
# as an MD5 hash and then converted to hexadecimal has n leading zeroes
# Part 1: 5 zeroes
# Part 2: 6 zeroes
from Crypto.Hash import MD5

answer = 1
found = False
key = 'yzbqklnj'
while found == False:
    keyAndAnswer = key+str(answer)
    h = MD5.new(keyAndAnswer)
    hd = h.hexdigest()
    # Part 1
    # if hd[0:5] == '00000':
    # Part 2
    if hd[0:6] == '000000':
        print hd
        print 'Answer = {}'.format(answer)
        found = True
    else:
        answer += 1


