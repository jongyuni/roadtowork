from collections import defaultdict, deque

N = int(input())
A, B = map(int, input().split())
M = int(input())
chons = defaultdict(list)
visited = [-1] * (N + 1)
que = deque()

for _ in range(M):
    x, y = map(int, input().split())
    chons[x].append(y)
    chons[y].append(x)

que.append(A)
visited[A] = 0

while que:
    n = que.popleft()
    for j in chons[n]:
        if visited[j] == -1:
            visited[j] = visited[n] + 1
            if j == B:
                que = deque()
                break
            que.append(j)

print(visited[B])
