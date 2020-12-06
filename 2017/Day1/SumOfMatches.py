with open('input.txt','r') as f:
   input = f.read()
   f.close()
input = input[0:-1]
halfway = len(input)/2
input_2 = input + input[0:halfway]

sum = 0
for i in range(len(input)-1):
   if input[i] == input[i+1]:
      sum += int(input[i])
if input[0] == input[-1]:
   sum += int(input[0])
print(sum)

sum_2 = 0
for i in range(len(input)-1):
   if input_2[i] == input_2[i+halfway]:
      sum_2 += int(input_2[i])
print(sum_2)
