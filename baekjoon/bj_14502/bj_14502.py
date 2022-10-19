import sys, copy
from collections import deque
from itertools import combinations

N, M = map(int, input().split())
table = list()
virus = deque()
blanks = list()
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
answer = 0

for i in range(N):
    table.append(list(map(int, sys.stdin.readline().split())))
    for j in range(M):
        if table[i][j] == 0:
            blanks.append((i, j))
        elif table[i][j] == 2:
            virus.append((i, j))
        else:
            continue

for comb in combinations(blanks, 3):
    one, two, three = comb
    table[one[0]][one[1]] = 1
    table[two[0]][two[1]] = 1
    table[three[0]][three[1]] = 1
    que = copy.deepcopy(virus)
    tmp = copy.deepcopy(table)
    safe = 0
    while que:
        i, j = que.popleft()
        for x, y in directions:
            a = i + x
            b = j + y
            if 0 <= a < N and 0 <= b < M:
                if tmp[a][b] == 0:
                    tmp[a][b] = 2
                    que.append((a, b))

    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 0:
                safe += 1

    answer = max(answer, safe)

    table[one[0]][one[1]] = 0
    table[two[0]][two[1]] = 0
    table[three[0]][three[1]] = 0

print(answer)
