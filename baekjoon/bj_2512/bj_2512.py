import sys
from collections import deque

N = int(input())
requests = deque(map(int, sys.stdin.readline().split()))
limit = int(input())
start = 0
end = max(requests)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for req in requests:
        if req > mid:
            total += mid
        else:
            total += req
    if total <= limit:
        start = mid + 1
    else:
        end = mid - 1

print(end)
