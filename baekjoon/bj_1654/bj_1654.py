from collections import deque

K, N = map(int, input().split())

owns = deque()
end = 0
start = 1

for _ in range(K):
    tmp = int(input())
    owns.append(tmp)

end = max(owns)

while start <= end:
    count = 0
    mid = (end + start) // 2

    for o in owns:
        count += (o // mid)

    if count >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
