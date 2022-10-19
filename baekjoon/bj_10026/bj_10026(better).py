import sys
from collections import deque

N = int(input())
table = list()

for _ in range(N):
    table.append(list(sys.stdin.readline().strip()))

visited = [[False] * N for _ in range(N)]
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
general = 0
special = 0


def bfs(i, j):
    que = deque()
    que.append((i, j))
    visited[i][j] = True
    k = table[i][j]
    while que:
        ni, nj = que.popleft()
        for x, y in directions:
            a = ni + x
            b = nj + y
            if 0 <= a < N and 0 <= b < N and visited[a][b] is False:
                if table[a][b] == k:
                    que.append((a, b))
                    visited[a][b] = True


for i in range(N):
    for j in range(N):
        if visited[i][j]:
            continue
        bfs(i, j)
        general += 1

visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if table[i][j] == 'R':
            table[i][j] = 'G'

for i in range(N):
    for j in range(N):
        if visited[i][j]:
            continue
        bfs(i, j)
        special += 1

print(general, special)
