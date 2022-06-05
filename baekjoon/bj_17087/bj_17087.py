import sys
import math

N, X = map(int,input().split())
A = list(map(int,sys.stdin.readline().split()))
cases = [abs(X-a) for a in A]

ans = cases[0]
for i in range(1,N):
  ans = math.gcd(ans,cases[i])

print(ans)
