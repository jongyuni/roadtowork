import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
friend = [[] for _ in range(N+1)]
bacon = [[0 for _ in range(N+1)] for _ in range(N+1)]
answer = []

for _ in range(M):
    i, j = map(int, input().split())
    friend[i].append(j)
    friend[j].append(i)

for i in range(1, N+1):
    q = deque()
    b = 1
    q.append((i, b))
    while q:
        now, bac = q.popleft()
        for next in friend[now]:
            if next == i:
                continue
            if bacon[i][next] != 0:
                continue
            bacon[i][next] = bac
            q.append((next, bac+1))

bacon_sum = []
for i in range(1, N+1):
    bacon_sum.append(sum(bacon[i]))

pivot = bacon_sum[0]
for i in range(1, N):
    pivot = min(pivot, bacon_sum[i])

for i in range(N):
    if pivot == bacon_sum[i]:
        answer.append(i+1)
answer.sort()
print(answer[0])
