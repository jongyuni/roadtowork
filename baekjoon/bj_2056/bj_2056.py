import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
times = [0 for _ in range(n + 1)]
que = deque()
timeline = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    tmp = list(map(int, input().split()))
    times[i] = tmp[0]
    for j in range(2, 2 + tmp[1]):
        graph[tmp[j]].append(i)
        indegree[i] += 1

for i in range(1, n + 1):
    if indegree[i] == 0:
        que.append(i)
        timeline[i] = times[i]

while que:
    i = que.popleft()
    for j in graph[i]:
        indegree[j] -= 1
        timeline[j] = max(timeline[j], timeline[i] + times[j])
        if indegree[j] == 0:
            que.append(j)

print(max(timeline))
