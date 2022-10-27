import sys, heapq
from collections import defaultdict

N = int(input())
M = int(input())
value = defaultdict(list)
INF = sys.maxsize

for _ in range(M):
    s, e, w = list(map(int, sys.stdin.readline().split()))
    value[s].append((e, w))

start, end = map(int, sys.stdin.readline().split())
distance = [INF] * (N + 1)
distance[start] = 0
visited = [False] * (N + 1)
heap = list()
heapq.heappush(heap, (0, start))

while heap:
    weight, now = heapq.heappop(heap)

    if visited[now]:
        continue
    visited[now] = True
    for next, edge in value[now]:
        new_weight = weight + edge
        if not visited[next] and new_weight < distance[next]:
            distance[next] = new_weight
            heapq.heappush(heap, (new_weight, next))

print(distance[end])
