from collections import deque

N, M = map(int, input().split())
miro = list()
for _ in range(N):
    miro.append(list(map(int, input())))

que = deque()
que.append((0, 0))
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
x, y = 0, 0

while que:
    x, y = que.popleft()
    for px, py in directions:
        nx = x + px
        ny = y + py
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if miro[nx][ny] == 0:
            continue
        if miro[nx][ny] == 1:
            que.append((nx, ny))
            miro[nx][ny] = miro[x][y] + 1

print(miro[N-1][M-1])


