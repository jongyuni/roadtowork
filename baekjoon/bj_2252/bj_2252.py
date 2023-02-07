import sys
from collections import deque


n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]
answer = []
que = deque()

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

for i in range(1, n+1):
    if indegree[i] == 0:
        que.append(i)

while que:
    i = que.popleft()
    answer.append(i)
    for j in graph[i]:
        indegree[j] -= 1
        if indegree[j] == 0:
            que.append(j)

for a in answer:
    print(a, end=" ")
