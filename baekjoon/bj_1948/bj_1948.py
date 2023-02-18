import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
reverse_graph = [[] for _ in range(n + 1)]
result = [0 for _ in range(n + 1)]
que = deque()

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    reverse_graph[b].append((a, c))
    indegree[b] += 1

s, e = map(int, input().split())

for i in range(1, n + 1):
    if indegree[i] == 0:
        que.append(i)

while que:
    now = que.popleft()
    for next, value in graph[now]:
        indegree[next] -= 1
        result[next] = max(result[next], result[now] + value)
        if indegree[next] == 0:
            que.append(next)

que.append(e)
count = 0
visited = [False] * (n + 1)

while que:
    now = que.popleft()
    for next, value in reverse_graph[now]:
        if result[next] + value == result[now]:
            count += 1
            if not visited[next]:
                que.append(next)
                visited[next] = True


print(result[e])
print(count)
