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

heap = list()
heapq.heappush(heap, (start, 0))

while heap:
    now, weight = heapq.heappop(heap)

    if distance[now] < weight:
        continue

    for next, edge in value[now]:
        new_weight = weight + edge
        if new_weight < distance[next]:
            distance[next] = new_weight
            heapq.heappush(heap, (next, new_weight))

print(distance[end])
