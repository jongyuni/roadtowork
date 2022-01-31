import sys
import itertools

def GCD(a,b):
  if b > a:
    a, b = b, a

  while b != 0:
    n = a%b
    a = b
    b = n

  return a

N = int(input())
answer = []

for _ in range(N):
  input_case = list(map(int,sys.stdin.readline().split()))
  all_case = itertools.combinations(input_case[1:],2)
  ans = 0

  for case in all_case:
    a, b = case[0], case[1]
    ans += GCD(a,b)
  
  answer.append(ans)

for a in answer:
  print(a)
  
