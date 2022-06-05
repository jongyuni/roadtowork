import sys
numbers = []

while True:
  number = int(sys.stdin.readline())
  if number == 0:
    break
  numbers.append(number)

max_num = max(numbers)
prime = [True]*(max_num+1)

for i in range(2,int(max_num**0.5)+1):
  if prime[i]:
    for j in range(i*2,max_num+1,i):
      prime[j] = False

for num in numbers:
  for i in range(3,num,2):
    j = num - i
    if prime[i] and prime[j]:
      print(str(num) + " = " + str(i) + " + " + str(j))
      break
    
