import sys

input = sys.stdin.readline

n, m = map(int, input().split())
papers = []
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
cnt = 0
max_area = 0
visited = [[False for _ in range(m)] for _ in range(n)]
one = []

for i in range(n):
    tmp = list(map(int, input().split()))
    papers.append(tmp)
    for j in range(m):
        if papers[i][j] == 1:
            one.append((i, j))

for i, j in one:
    if visited[i][j]:
        continue
    stack = []
    area = 0
    stack.append((i, j))
    visited[i][j] = True
    while stack:
        ni, nj = stack.pop()
        area += 1
        for pi, pj in directions:
            x = ni + pi
            y = nj + pj
            if x < 0 or x >= n or y < 0 or y >= m:
                continue
            if papers[x][y] == 0 or visited[x][y]:
                continue
            visited[x][y] = True
            stack.append((x, y))

    cnt += 1
    max_area = max(max_area, area)

print(cnt)
print(max_area)
