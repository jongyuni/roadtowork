from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
fish = list()
cx, cy = 0, 0
size = [2, 0]
answer = 0

for i in range(N):
    fish.append(list(map(int, input().split())))
    for j in range(N):
        if fish[i][j] == 9:
            cx, cy = i, j
            fish[i][j] = 0

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(cx, cy, size):
    dests = list()
    distances = [[0] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    que = deque()
    que.append((cx, cy))
    visited[cx][cy] = True

    while que:
        x, y = que.popleft()

        for px, py in directions:
            nx, ny = x + px, y + py
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if fish[nx][ny] <= size:
                    que.append((nx, ny))
                    visited[nx][ny] = True
                    distances[nx][ny] = distances[x][y] + 1
                    if 0 < fish[nx][ny] < size:
                        dests.append((distances[nx][ny], nx, ny))
    return sorted(dests, key=lambda x: (x[0], x[1], x[2]))


while True:
    target = bfs(cx, cy, size[0])

    if not target:
        break

    fish[cx][cy] = 0
    cx, cy = target[0][1], target[0][2]
    fish[cx][cy] = 0
    size[1] += 1
    answer += target[0][0]

    if size[1] == size[0]:
        size[1] = 0
        size[0] += 1

print(answer)
