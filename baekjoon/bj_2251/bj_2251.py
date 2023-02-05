import sys
from collections import deque

input = sys.stdin.readline
capacity = list(map(int, input().split()))
visited = [[False for _ in range(201)] for _ in range(201)]
answer = []
ways = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]


def bfs():
    que = deque()
    answer.append(capacity[2])
    visited[0][0] = True
    que.append((0, 0))

    while que:
        a, b = que.popleft()
        c = capacity[2] - a - b
        for s, e in ways:
            next = [a, b, c]
            next[e] += next[s]
            next[s] = 0
            if next[e] > capacity[e]:
                next[s] += next[e] - capacity[e]
                next[e] = capacity[e]
            if not visited[next[0]][next[1]]:
                visited[next[0]][next[1]] = True
                que.append((next[0], next[1]))
                if next[0] == 0:
                    answer.append(capacity[2] - next[1])


bfs()
answer.sort()
for a in answer:
    print(a, end=' ')
