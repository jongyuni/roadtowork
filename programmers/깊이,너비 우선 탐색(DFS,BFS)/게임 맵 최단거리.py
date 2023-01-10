from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    lengths = [[0] * m for _ in range(n)]
    que = deque([(0, 0)])

    while que:
        x, y = que.popleft()

        if x == n - 1 and y == m - 1:
            break
        for px, py in directions:
            nx = x + px
            ny = y + py
            if 0 <= nx < n and 0 <= ny < m and lengths[nx][ny] == 0 and maps[nx][ny] == 1:
                que.append((nx, ny))
                lengths[nx][ny] = lengths[x][y] + 1

    if lengths[n - 1][m - 1] == 0:
        return -1
    else:
        return lengths[n - 1][m - 1] + 1
