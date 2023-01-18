import heapq, sys


def solution(N, road, K):
    answer = 0
    M = int(sys.maxsize)
    graph = [[M] * (N + 1) for _ in range(N + 1)]
    que = []
    visited = [False] * (N + 1)

    for ro in road:
        s, e, v = ro
        graph[s][e] = min(graph[s][e], v)
        graph[e][s] = min(graph[e][s], v)

    cost = [M] * (N + 1)
    cost[1] = 0
    heapq.heappush(que, (0, 1))

    while que:
        v, i = heapq.heappop(que)

        if visited[i]:
            continue

        visited[i] = True

        for e in range(1, N + 1):
            new_v = graph[i][e]
            cost[e] = min(cost[e], v + new_v)
            heapq.heappush(que, (cost[e], e))

    for c in cost:
        if c <= K:
            answer += 1

    return answer
