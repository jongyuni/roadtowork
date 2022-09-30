import sys
from collections import deque

N = int(sys.stdin.readline())

que = deque()

for i in range(1, N + 1):
    que.append(i)

cnt = 1
while len(que) > 1:
    if cnt % 2 == 1:
        que.popleft()
    else:
        t = que.popleft()
        que.append(t)
    cnt += 1


print(que[0])
