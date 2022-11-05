import sys
from collections import defaultdict

input = sys.stdin.readline
N = int(input())
trees = defaultdict(list)
answer = 0
visited = [False] * (N + 1)
distance = [0] * (N + 1)

for _ in range(N - 1):
    i, j, k = map(int, input().split())
    trees[i].append((j, k))
    trees[j].append((i, k))


def dfs(i):
    global answer
    stack = list()
    stack.append(i)
    max_distance = 0
    max_idx = 0
    while stack:
        x = stack.pop()
        visited[x] = True
        for y, z in trees[x]:
            if not visited[y]:
                distance[y] = distance[x] + z
                stack.append(y)
                if distance[y] > max_distance:
                    max_distance = distance[y]
                    max_idx = y

    return max_idx

next_idx = dfs(1)
visited = [False] * (N + 1)
distance = [0] * (N + 1)
print(distance[dfs(next_idx)])
