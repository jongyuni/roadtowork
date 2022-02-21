import sys
N = int(sys.stdin.readline())
dp = [x for x in range(N+1)]

for i in range(1,N+1):
  for j in range(1,int(i**0.5)+1):
    if dp[i] > dp[i-j*j]+1:
      dp[i] = dp[i-j*j]+1
      
print(dp[N])
