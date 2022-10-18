from collections import deque
import sys

directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
answers = []
while True:
    w, h = map(int, input().split())
    answer = 0
    if w == 0 and h == 0:
        break
    table = list()

    for _ in range(h):
        table.append(list(map(int, sys.stdin.readline().split())))

    for i in range(h):
        for j in range(w):
            que = deque()
            que.append((i, j))
            island = set()
            while que:
                a, b = que.popleft()
                if table[a][b] != 1:
                    continue
                table[a][b] += 1
                island.add((a, b))
                for x, y in directions:
                    m = a + x
                    n = b + y

                    if m < 0 or n < 0 or m >= h or n >= w:
                        continue

                    if table[m][n] != 1:
                        continue

                    que.append((m, n))
            if island:
                answer += 1

    answers.append(answer)

for ans in answers:
    print(ans)
