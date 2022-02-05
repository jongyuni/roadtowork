import sys

N = int(sys.stdin.readline())
case = list(map(int,sys.stdin.readline().split()))
d = [1] *N

for i in range(N):
  for j in range(i):
    if case[i] > case[j]:
      d[i] = max(d[i],d[j]+1)

print(max(d))
