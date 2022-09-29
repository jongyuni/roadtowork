import sys

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
S = [numbers[0]]
R = [0] * M

for i in range(1, N):
    S.append(S[i-1] + numbers[i])

for i in range(N):
    R[S[i] % M] += 1

answer = R[0]

for r in R:
    answer += r * (r-1) // 2

print(answer)
