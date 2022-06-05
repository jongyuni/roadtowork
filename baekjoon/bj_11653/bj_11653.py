import sys

N = int(sys.stdin.readline())
prime = [False, False] + [True] * (N-1)

for i in range(2, int(N**0.5)+1):
  if prime[i]:
    for j in range(i*2,N+1,i):
      prime[j] = False

if N == 1:
  print("")
else:
  while not prime[N]:
    for i in range(2,N):
      if not N%i and prime[i]:
        print(i)
        N //= i
        break
  print(N)
