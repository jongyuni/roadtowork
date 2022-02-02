import sys

A, B = map(int,sys.stdin.readline().split())
R = [i for i in range(30)]
M = int(sys.stdin.readline())
N = list(map(int,sys.stdin.readline().split()))
value = 0
answer = ""

for i in range(M):
  value += N[i] * A**(M-1-i)

x, y = 0, 0
while value >= B:
  x = value // B
  y = value % B
  answer = str(y)+ " " + answer
  value = x

answer = str(value) + " " + answer
print(answer) 
