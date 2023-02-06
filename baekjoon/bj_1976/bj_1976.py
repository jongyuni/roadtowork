import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i] = list(map(int, sys.stdin.readline().split()))
    graph[i].insert(0, 0)

plan = list(map(int, sys.stdin.readline().split()))
parent = [i for i in range(n + 1)]


def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[a] = b


for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == 1:
            union(i, j)

pivot = find(plan[0])
for i in range(1, m):
    if pivot != find(plan[i]):
        print("NO")
        break
else:
    print("YES")
