from collections import deque
MAX_SIZE = 100001
N, K = map(int, input().split())

road = [0] * MAX_SIZE

que = deque()
que.append(N)
while que:
    n = que.popleft()
    if n == K:
        break
    if 0 <= (n-1) and road[n-1] == 0:
        que.append(n-1)
        road[n-1] = road[n] + 1
    if (n+1) < MAX_SIZE and road[n+1] == 0:
        que.append(n+1)
        road[n+1] = road[n] + 1
    if 0 <= 2*n < MAX_SIZE and road[2*n] == 0:
        que.append(2*n)
        road[2*n] = road[n] + 1


print(road[K])
