from collections import deque

M, N = map(int, input().split())
storages = list()
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
bad = set()
good = deque()
answer = 0
flag = True

for _ in range(N):
    storages.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if storages[i][j] == -1:
            continue
        elif storages[i][j] == 0:
            bad.add((i, j))
        else:
            good.append((i, j))
while flag:
    nextgood = deque()
    while good:
        i, j = good.popleft()
        for x, y in directions:
            if (i + x, j + y) in bad:
                bad.remove((i + x, j + y))
                nextgood.append((i + x, j + y))
    good.extend(nextgood)
    if not good:
        flag = False
        if bad:
            answer = -1
    else:
        answer += 1

print(answer)
