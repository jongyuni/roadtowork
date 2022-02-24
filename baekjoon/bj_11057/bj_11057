import sys
N = int(sys.stdin.readline())
dp = [1] * 10

for _ in range(1, N):
  for i in range(1,10):
    dp[i] = (dp[i] + dp[i-1]) 

print(sum(dp)% 10007)
