import sys

N = int(sys.stdin.readline())
d = [0, 1, 2]+[0] * (N-2)

for i in range(3,N+1):
  d[i] = d[i-1] + d[i-2]


print(d[N]%10007)
