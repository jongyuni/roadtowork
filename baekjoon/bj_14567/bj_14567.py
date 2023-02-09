import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
que = deque()
answer = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

for i in range(1, n + 1):
    if indegree[i] == 0:
        que.append(i)
        answer[i] = 1

while que:
    i = que.popleft()
    for j in graph[i]:
        indegree[j] -= 1
        if indegree[j] == 0:
            que.append(j)
            answer[j] = max(answer[j], answer[i] + 1)

for i in range(1, n + 1):
    print(answer[i], end=" ")
