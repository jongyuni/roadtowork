X, Y = map(int, input().split())

original_rate = int(100 * Y / X)

start = 1
end = X
ans = -1

while start <= end:
    mid = (start + end) // 2
    new_rate = int(100 * (Y + mid) / (X + mid))
    if new_rate > original_rate:
        end = mid - 1
        ans = mid
    else:
        start = mid + 1

print(ans)
