def solution(n):
    dp = [0] * (n + 1)
    dp[2] = 3
    if n > 2:
        dp[4] = 11
        for i in range(5, n + 1):
            if i % 2 == 1:
                continue
            dp[i] = dp[i - 2] * 3 + 2
            for j in range(i - 4, -1, -2):
                dp[i] += dp[j] * 2
            dp[i] = dp[i] % 1000000007

    return dp[n]
