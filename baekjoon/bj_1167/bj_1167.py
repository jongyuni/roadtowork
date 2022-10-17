from collections import deque
import sys

V = int(input())
trees = [[] for _ in range(V + 1)]
answer = 0
distance = [0] * (V + 1)

for _ in range(V):
    tmp = list(map(int, sys.stdin.readline().split()))
    i = tmp[0]
    j = 1
    while True:
        if tmp[j] == -1:
            break
        trees[i].append((tmp[j], tmp[j + 1]))
        j += 2


def bfs(i):
    que = deque()
    que.append(i)
    max_dist = 0
    max_idx = 0
    while que:
        n = que.popleft()
        for idx, val in trees[n]:
            if idx == i:
                continue
            if distance[idx] != 0:
                continue
            distance[idx] = distance[n] + val
            que.append(idx)
            if distance[idx] >= max_dist:
                max_idx = idx
                max_dist = distance[idx]

    return max_idx


next_idx = bfs(1)
distance = [0] * (V + 1)
print(distance[bfs(next_idx)])
