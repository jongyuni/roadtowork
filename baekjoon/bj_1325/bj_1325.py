import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
belief = [0] * (n + 1)
t = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)


def bfs(s):
    visited = [False] * (n + 1)
    que = deque()
    visited[s] = True
    que.append(s)

    while que:
        i = que.popleft()
        for j in graph[i]:
            if visited[j]:
                continue
            que.append(j)
            visited[j] = True
            belief[j] += 1


for i in range(1, n + 1):
    bfs(i)

for i in range(1, n + 1):
    t = max(t, belief[i])

for i in range(1, n + 1):
    if belief[i] == t:
        print(i, end=' ')
