import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
directions = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (2, -1), (1, -2), (2, 1), (1, 2)]

for _ in range(t):
    l = int(input())
    que = deque()
    sx, sy = map(int, input().split())
    tx, ty = map(int, input().split())
    visited = [[0] * l for _ in range(l)]
    que.append((sx, sy))
    visited[sx][sy] = 1

    while que:
        sx, sy = que.popleft()
        if sx == tx and sy == ty:
            print(visited[sx][sy] - 1)
            break

        for px, py in directions:
            nx = sx + px
            ny = sy + py
            if 0 <= nx < l and 0 <= ny < l and visited[nx][ny] == 0:
                que.append((nx, ny))
                visited[nx][ny] = visited[sx][sy] + 1
