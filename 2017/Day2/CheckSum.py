def returnDiv(row):
    for j in range(len(row)):
        for k in range(j+1,len(row)):
            if row[j] % row[k] == 0:
                return row[j]/row[k]


with open('input.txt','r') as f:
   input = [map(int, line.split()) for line in f]
   f.close()
checkSum = 0
checkDiv = 0
for i in range(len(input)):
    checkSum += max(input[i]) - min(input[i])
    input[i].sort()
    checkDiv += returnDiv(input[i][::-1])

print(checkSum)
print(checkDiv)

