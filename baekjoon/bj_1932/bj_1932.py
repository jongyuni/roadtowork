import sys
n = int(sys.stdin.readline())
tri = []
dp = []

for _ in range(n):
  tmp = list(map(int,sys.stdin.readline().split()))
  tri.append(tmp)
  dp.append([0]*len(tmp))
dp[0] = tri[0]

for i in range(1,n):
  for j in range(len(tri[i])):
    if j == 0:
      dp[i][j] = dp[i-1][j] + tri[i][j]
    elif j == len(tri[i])-1:
      dp[i][j] = dp[i-1][j-1] + tri[i][j]
    else:
      dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + tri[i][j]

print(max(dp[-1]))
