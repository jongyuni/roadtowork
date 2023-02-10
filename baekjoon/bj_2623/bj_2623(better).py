import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
cycle = False
answer = []
que = deque()

for _ in range(m):
    tmp = list(map(int, input().split()))
    for i in range(1, tmp[0]):
        graph[tmp[i]].append(tmp[i + 1])
        indegree[tmp[i + 1]] += 1

for i in range(1, n + 1):
    if indegree[i] == 0:
        que.append(i)

while que:
    i = que.popleft()
    answer.append(i)
    for j in graph[i]:
        indegree[j] -= 1
        if indegree[j] == 0:
            que.append(j)

if len(answer) != n:
    print(0)
else:
    for a in answer:
        print(a)
