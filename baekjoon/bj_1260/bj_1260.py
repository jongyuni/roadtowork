from collections import deque
N, M, V = map(int, input().split())
queue = deque()
visited = [False] * (N+1)
A = [[] for _ in range(N+1)]

for _ in range(M):
  s, e = map(int,input().split())
  A[s].append(e)
  A[e].append(s)

for lst in A:
  lst.sort()

def dfs(v):
  print(v, end=' ')
  visited[v] = True
  for i in A[v]:
    if not visited[i]:
      dfs(i)

def bfs(v):
  queue.append(v)
  visited[v] = True
  while queue:
    n = queue.popleft()
    print(n, end=' ')
    for i in A[n]:
      if not visited[i]:
        visited[i] = True
        queue.append(i)
  
dfs(V)
print()
visited = [False] * (N+1)
bfs(V)
