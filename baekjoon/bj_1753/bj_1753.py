from collections import defaultdict
import heapq, sys

V, E = map(int, input().split())
S = int(input())
value = defaultdict(list)
distance = [400000000] * (V + 1)
distance[S] = 0
visited = [False] * (V + 1)

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    value[u].append((w, v))

que = list()
heapq.heappush(que, (0, S))

while len(que) > 0:
    c, now = heapq.heappop(que)
    if visited[now]:
        continue
    visited[now] = True
    for weight, next in value[now]:
        if distance[next] > distance[now] + weight:
            distance[next] = distance[now] + weight
            heapq.heappush(que, (distance[next], next))

for a in range(1, V + 1):
    if distance[a] == 400000000:
        print('INF')
    else:
        print(distance[a])
