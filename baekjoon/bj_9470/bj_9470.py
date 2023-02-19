import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k, m, p = map(int, input().split())
    graph = [[] for _ in range(m + 1)]
    indegree = [0] * (m + 1)
    strahler = [[0, 0] for _ in range(m + 1)]
    que = deque()

    for _ in range(p):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    for i in range(1, m + 1):
        if indegree[i] == 0:
            que.append(i)
            strahler[i][0] = 1
            strahler[i][1] = 0

    while que:
        now = que.popleft()
        for next in graph[now]:
            indegree[next] -= 1
            if strahler[next][0] == strahler[now][0]:
                strahler[next][1] += 1
            elif strahler[next][0] < strahler[now][0]:
                strahler[next][0] = strahler[now][0]
                strahler[next][1] = 1

            if indegree[next] == 0:
                if strahler[next][1] > 1:
                    strahler[next][0] += 1
                que.append(next)

    print(k, strahler[m][0])
