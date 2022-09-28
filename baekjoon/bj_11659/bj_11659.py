import sys

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
S = [0 for _ in range(N+1)]

for i in range(1, N+1):
    S[i] = S[i-1] + numbers[i-1]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(S[j] - S[i-1])
