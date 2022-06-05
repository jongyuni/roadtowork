import sys
n = int(sys.stdin.readline())
wines = []
dp = [[0]*3 for i in range(n)]
for _ in range(n):
  wines.append(int(sys.stdin.readline()))
dp[0] = [0,wines[0],0]
for i in range(1,n):
  dp[i][0] = max(dp[i-1])
  dp[i][1] = dp[i-1][0] + wines[i]
  dp[i][2] = dp[i-1][1] + wines[i]

print(max(dp[-1]))
