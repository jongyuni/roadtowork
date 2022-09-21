import sys
sys.setrecursionlimit(10000)
N, M = map(int, sys.stdin.readline().split())
visited = [False] * (N+1)
adjoin_list = [[] for _ in range(N+1)]

for _ in range(M):
  p1, p2 = map(int, sys.stdin.readline().split())
  adjoin_list[p1].append(p2)
  adjoin_list[p2].append(p1)

def dfs(i):
  visited[i] = True
  for j in adjoin_list[i]:
    if not visited[j]:
      dfs(j)
  

cnt = 0
for i in range(1, N+1):
  if not visited[i]:
    cnt += 1
    dfs(i)

print(cnt)
