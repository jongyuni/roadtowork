import sys
from collections import deque

t = int(sys.stdin.readline())
answer = []

for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())

    times = list(map(int, sys.stdin.readline().split()))
    times.insert(0, 0)

    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    que = deque()

    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        indegree[b] += 1
        graph[a].append(b)

    w = int(sys.stdin.readline())
    built_time = [0] * (n + 1)
    for i in range(1, n + 1):
        if indegree[i] == 0:
            que.append(i)
            built_time[i] = times[i]

    while que:
        i = que.popleft()
        for j in graph[i]:
            indegree[j] -= 1
            built_time[j] = max(built_time[j], built_time[i])
            if indegree[j] == 0:
                que.append(j)
                built_time[j] += times[j]

    answer.append(built_time[w])

for a in answer:
    print(a)
