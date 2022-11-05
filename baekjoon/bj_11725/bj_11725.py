import sys
from collections import defaultdict

input = sys.stdin.readline
N = int(input())
trees = defaultdict(list)
answer = [0] * (N + 1)
visited = [False] * (N + 1)
stack = []

for _ in range(N - 1):
    i, j = map(int, input().split())
    trees[i].append(j)
    trees[j].append(i)

stack.append(1)

while stack:
    i = stack.pop()
    visited[i] = True
    for j in trees[i]:
        if not visited[j]:
            stack.append(j)
        else:
            answer[i] = j

for i in range(2, N + 1):
    print(answer[i])
