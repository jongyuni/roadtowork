import sys
N, M = list(map(int,sys.stdin.readline().split()))

def prime(number):
  for x in range(2, int(number**0.5)+1):
    if number % x == 0:
      return False
  else:
    return True
      

for i in range(N,M+1):
  if i == 1:
    continue
  elif i == 2:
    print(i)
    continue
  elif i % 2 == 0:
    continue
  elif i == 3:
    print(i)
    continue

  if prime(i):
    print(i)
