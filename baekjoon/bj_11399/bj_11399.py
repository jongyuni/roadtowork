import sys

N = int(input())
times = list(map(int, sys.stdin.readline().split()))
times.sort()
answer = 0

for i in range(1, N):
    times[i] += times[i-1]

for t in times:
    answer += t

print(answer)
