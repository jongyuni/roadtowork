N = int(input())
K = int(input())

start = 1
end = K
ans = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(1, N + 1):
        cnt += min(N, mid // i)

    if cnt >= K:
        end = mid - 1
        ans = mid
    else:
        start = mid + 1


print(ans)
