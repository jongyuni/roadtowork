import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
table = list()
cheeses = list()
answer = 0
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i in range(N):
    table.append(list(map(int, input().split())))
    for j in range(M):
        if table[i][j] == 1:
            cheeses.append((i, j))


def findouterair():
    que = deque()
    que.append((0, 0))
    outerair = [[1] * M for _ in range(N)]
    outerair[0][0] = 0
    while que:
        i, j = que.popleft()
        for pi, pj in directions:
            ni = i + pi
            nj = j + pj
            if table[ni][nj] == 0 and not outerair[ni][nj] == 0:
                que.append((ni, nj))
                outerair[ni][nj] = 0

    return outerair


c = len(cheeses)
while c > 0:
    outerair = findouterair()
    que = deque()
    for cheese in cheeses:
        i, j = cheese
        count = 0
        if table[i][j] == 0:
            continue
        for pi, pj in directions:
            ni = i + pi
            nj = j + pj
            if 0 <= ni < N and 0 <= nj < M and outerair[ni][nj] == 0:
                count += 1
        if count > 1:
            que.append((i, j))
    while que:
        i, j = que.popleft()
        table[i][j] = 0
        c -= 1

    answer += 1

print(answer)
