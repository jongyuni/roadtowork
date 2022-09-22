import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline
N, M = map(int, input().split())
checked = [False]*(N+1)
P = [[] for _ in range(N+1)]
depth = 0
answer = False

for _ in range(M):
  a, b = map(int, input().split())
  P[a].append(b) 
  P[b].append(a)

def dfs(number,depth):
  global answer
  if depth == 4:
    answer = True
    return
  checked[number] = True
  for i in P[number]:
    if not checked[i]:
      dfs(i,depth+1)
  checked[number] = False
    
    
for i in range(N):
  dfs(i, depth)
  if answer:
    break
  else:
    depth = 0
  
if answer:
  print(1)
else:
  print(0)
