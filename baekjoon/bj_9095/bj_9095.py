import sys

N = int(sys.stdin.readline())
case = []
M = 0
d = [0, 1, 2, 4]

for _ in range(N):
  n = int(sys.stdin.readline())
  case.append(n)
  if n > M:
    M = n

for i in range(4,M+1):
  d.append(d[i-1] + d[i-2] + d[i-3])

for i in range(N):
  print(d[case[i]])
