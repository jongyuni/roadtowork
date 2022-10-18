from collections import deque
import sys

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
N = int(input())
table = list()
answer = 0
max_h = 0
for i in range(N):
    table.append(list(map(int, sys.stdin.readline().split())))
    for j in range(N):
        if table[i][j] > max_h:
            max_h = table[i][j]


def bfs(i, j, h, visited):
    que = deque()
    que.append((i, j))
    visited[i][j] = 1
    while que:
        a, b = que.popleft()
        for x, y in directions:
            m = a + x
            n = b + y
            if 0 <= m < N and 0 <= n < N:
                if visited[m][n] == 0 and table[m][n] >= h:
                    visited[m][n] = 1
                    que.append((m, n))


for h in range(1, max_h + 1):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if table[i][j] >= h and visited[i][j] == 0:
                bfs(i, j, h, visited)
                cnt += 1

    answer = max(answer, cnt)

print(answer)
