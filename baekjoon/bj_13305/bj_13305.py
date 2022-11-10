import sys

N = int(input())
paths = list(map(int, sys.stdin.readline().split()))
oils = list(map(int, sys.stdin.readline().split()))
min_oil = int(sys.maxsize)
answer = 0

for i in range(N - 1):
    min_oil = min(min_oil, oils[i])
    answer += min_oil * paths[i]

print(answer)
