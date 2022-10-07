from collections import deque

N = int(input())

tree = [deque() for _ in range(N+1)]
tree[0].append(0)
visited = set()
M = int(input())

for _ in range(M):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

que = deque()
que.append(1)

while que:
    start = que.popleft()
    while tree[start]:
        next = tree[start].popleft()
        if next not in visited:
            que.append(next)
            visited.add(next)
        else:
            continue

print(len(visited)-1)
