N = int(input())
answer = 0
dp = [0] * (N + 1)

if N == 3:
    answer = 1
elif N == 4:
    answer = -1
elif N > 4:
    dp[0] = -1
    dp[1] = -1
    dp[2] = -1
    dp[3] = 1
    dp[4] = -1
    dp[5] = 1
    for i in range(6, N + 1):
        if dp[i - 3] < 0 and dp[i - 5] < 0:
            dp[i] = -1
        elif dp[i - 3] < 0 and dp[i - 5] > 0:
            dp[i] = dp[i - 5] + 1
        elif dp[i - 3] > 0 and dp[i - 5] < 0:
            dp[i] = dp[i - 3] + 1
        else:
            dp[i] = min(dp[i - 3], dp[i - 5]) + 1
    answer = dp[N]

print(answer)
