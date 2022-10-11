from collections import deque

N = int(input())
houses = list()
visited = set()
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for _ in range(N):
    houses.append(list(map(int, input())))
que = deque()
for i in range(N):
    for j in range(N):
        if houses[i][j] == 1:
            que.append((i, j))
a = 0
answers = []
while que:
    i, j = que.popleft()
    if (i, j) in visited:
        continue
    nextque = deque()
    nextque.append((i, j))
    b = 0
    while nextque:
        b += 1
        i, j = nextque.popleft()
        visited.add((i, j))
        for px, py in directions:
            x = i + px
            y = j + py
            if x < 0 or y < 0 or x >= N or y >= N:
                continue
            if houses[x][y] == 1 and (x, y) not in visited:
                houses[x][y] += 1
                nextque.append((x, y))
    a += 1
    answers.append(b)

print(a)
answers.sort()
for ans in answers:
    print(ans)
