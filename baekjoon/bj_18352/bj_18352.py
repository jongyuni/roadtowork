import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
answer = []
visited = [-1] * (n + 1)
que = deque()

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)


def bfs(x):
    que = deque()
    que.append(x)
    visited[x] += 1
    while que:
        now = que.popleft()
        for i in graph[now]:
            if visited[i] == -1:
                visited[i] = visited[now] + 1
                que.append(i)


bfs(x)

for i in range(1, n + 1):
    if visited[i] == k:
        answer.append(i)

if answer:
    answer.sort()
    for a in answer:
        print(a)
else:
    print(-1)
