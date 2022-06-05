import sys
N = int(sys.stdin.readline())
cases = list(map(int,sys.stdin.readline().split()))
d = [-1001]

for i in range(N):
  d.append(max(d[-1]+cases[i],cases[i]))

print(max(d))
