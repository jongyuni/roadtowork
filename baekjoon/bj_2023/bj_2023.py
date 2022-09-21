import sys
sys.setrecursionlimit(10000)
N = int(input())

def isPrime(number):
  for i in range(2,number//2+1):
    if number % i == 0:
      return False
  return True

def dfs(n):
  if len(str(n)) == N:
    print(n)
  else:
    for i in range(1,10):
      if i % 2 == 0:
        continue
      if isPrime(n*10+i):
        dfs(n*10+i)
      else:
        continue
  
  
dfs(2)
dfs(3)
dfs(5)
dfs(7)
