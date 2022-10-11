from collections import deque

M, N, H = map(int, input().split())
storages = list()
directions = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]
bad = set()
good = deque()
answer = 0
flag = True

for _ in range(N*H):
    storages.append(list(map(int, input().split())))

for i in range(N*H):
    for j in range(M):
        if storages[i][j] == -1:
            continue
        elif storages[i][j] == 0:
            bad.add((i%N, j, i//N))
        else:
            good.append((i%N, j, i//N))
while flag:
    nextgood = deque()
    while good:
        i, j, k = good.popleft()
        for x, y, z in directions:
            if (i + x, j + y, k + z) in bad:
                bad.remove((i + x, j + y, k + z))
                nextgood.append((i + x, j + y, k + z))
    good.extend(nextgood)
    if not good:
        flag = False
        if bad:
            answer = -1
    else:
        answer += 1

print(answer)
