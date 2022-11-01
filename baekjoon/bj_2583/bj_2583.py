from collections import deque

m, n, k = map(int, input().split())
s = [[0] * n for i in range(m)]
directions = [(1,0),(0,1),(-1,0),(0,-1)]
cnt = []

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            s[i][j] = 1

for i in range(m):
    for j in range(n):
        if s[i][j] != 0:
            continue
        que = deque()
        que.append((i,j))
        s[i][j] += 1
        tmp = 0
        while que:
            x, y = que.popleft()
            tmp += 1
            for px, py in directions:
                a = x + px
                b = y + py
                if 0 <= a < m and 0 <= b < n:
                    if s[a][b] == 0:
                        que.append((a,b))
                        s[a][b] += 1
        cnt.append(tmp)

cnt.sort()
print(len(cnt))
for c in cnt:
    print(c,end=' ')
