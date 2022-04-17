import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [[0]*N for _ in range(2)]
dp[0][0] = arr[0]
ans = arr[0]
for i in range(1, N):
  dp[0][i] = max(dp[0][i-1]+arr[i],arr[i])
  dp[1][i] = max(dp[0][i-1],dp[1][i-1]+arr[i])
  ans = max(ans, dp[0][i], dp[1][i])

print(ans)
