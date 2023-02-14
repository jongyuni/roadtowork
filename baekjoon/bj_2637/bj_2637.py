import sys
from collections import deque

n = int(sys.stdin.readline())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
nums = [[0] * (n + 1) for _ in range(n + 1)]
m = int(sys.stdin.readline())
que = deque()
basic = set()

for _ in range(m):
    x, y, k = map(int, sys.stdin.readline().split())
    indegree[x] += 1
    graph[y].append((x, k))

for i in range(1, n + 1):
    if indegree[i] == 0:
        que.append(i)
        basic.add(i)

while que:
    i = que.popleft()
    for j, k in graph[i]:
        if i in basic:
            nums[j][i] += k
        else:
            for a in range(1, n+1):
                nums[j][a] += nums[i][a] * k
        indegree[j] -= 1
        if indegree[j] == 0:
            que.append(j)

for idx, val in enumerate(nums[n]):
    if val > 0:
        print(idx, val)

