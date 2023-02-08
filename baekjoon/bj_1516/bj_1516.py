import sys
from collections import deque

n = int(sys.stdin.readline())
time = [0] * (n + 1)
base = [0] * (n + 1)
indegree = [0] * (n + 1)
que = deque()
answer = []
graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    tmp = list(map(int, sys.stdin.readline().split()))
    time[i] = tmp[0]
    for j in range(1, len(tmp)):
        if tmp[j] == -1:
            break
        indegree[i] += 1
        graph[tmp[j]].append(i)
    if indegree[i] == 0:
        que.append(i)

while que:
    i = que.popleft()
    for j in graph[i]:
        indegree[j] -= 1
        base[j] = max(base[j], base[i] + time[i])
        if indegree[j] == 0:
            que.append(j)

for i in range(1, n + 1):
    print(base[i] + time[i])
