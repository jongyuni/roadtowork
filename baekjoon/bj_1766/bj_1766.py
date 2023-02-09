import sys, heapq

input = sys.stdin.readline
n, m = map(int, input().split())
indegree = [0] * (n+1)
graph = [set() for _ in range(n+1)]
answer = []
que = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    indegree[b] += 1

for i in range(1, n+1):
    if indegree[i] == 0:
        que.append(i)


while que:
    i = heapq.heappop(que)
    answer.append(i)
    for j in graph[i]:
        indegree[j] -= 1
        if indegree[j] == 0:
            heapq.heappush(que, j)

for a in answer:
    print(a, end=" ")

