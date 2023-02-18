import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    last_year = list(map(int, input().split()))
    graph = [set() for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    que = deque()
    result = []

    for i in range(n):
        for j in range(i + 1, n):
            graph[last_year[i]].add(last_year[j])
            indegree[last_year[j]] += 1

    c = int(input())
    for _ in range(c):
        a, b = map(int, input().split())

        if a in graph[b]:
            graph[b].remove(a)
            indegree[a] -= 1
            graph[a].add(b)
            indegree[b] += 1
        else:
            graph[a].remove(b)
            indegree[b] -= 1
            graph[b].add(a)
            indegree[a] += 1

    for i in range(1, n + 1):
        if indegree[i] == 0:
            que.append(i)

    if not que:
        print("IMPOSSIBLE")
        continue

    while que:
        now = que.popleft()
        result.append(now)
        for next in graph[now]:
            indegree[next] -= 1
            if indegree[next] == 0:
                que.append(next)

    if sum(indegree) != 0:
        print("IMPOSSIBLE")
    else:
        print(*result)

