import sys

N = int(sys.stdin.readline())
d = [0, 1, 3]

for i in range(3,N+1):
  d.append(d[i-1] + d[i-2]*2)


print(d[N]%10007)
