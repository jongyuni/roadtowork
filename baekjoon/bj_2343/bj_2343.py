import sys
from collections import deque

N, M = map(int, input().split())

lectures = deque(map(int, sys.stdin.readline().split()))

end = sum(lectures)
start = max(lectures)

while start <= end:
    mid = (start + end) // 2
    total = 0
    count = 0
    for lec in lectures:
        if total + lec > mid:
            count += 1
            total = 0
        total += lec
    if total != 0:
        count += 1
    if count > M:
        start = mid + 1
    else:
        end = mid - 1

print(start)
