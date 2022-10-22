import sys
from collections import deque

N, M = map(int, input().split())
table = list()
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
road = [[[0, 0] for _ in range(M)] for _ in range(N)]

for _ in range(N):
    table.append(list(map(int, sys.stdin.readline().strip())))


def bfs():
    que = deque()
    que.append((0, 0, 0))
    road[0][0][0] = 1

    while que:
        i, j, k = que.popleft()
        if i == N - 1 and j == M - 1:
            return road[i][j][k]
        for x, y in directions:
            a = i + x
            b = j + y
            if 0 <= a < N and 0 <= b < M:
                if table[a][b] == 1 and k == 0:
                    road[a][b][1] = road[i][j][k] + 1
                    que.append((a, b, 1))
                    continue
                if table[a][b] == 0 and road[a][b][k] == 0:
                    road[a][b][k] = road[i][j][k] + 1
                    que.append((a, b, k))
                    continue
    return -1


print(bfs())
