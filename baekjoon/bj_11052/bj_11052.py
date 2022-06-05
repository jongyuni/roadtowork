import sys

N = int(sys.stdin.readline())
P = list(map(int,sys.stdin.readline().split()))
P.insert(0,0)

for i in range(2,N+1):
  for j in range(i):
    P[i] = max(P[j]+P[i-j],P[i])
  

print(P[N])
