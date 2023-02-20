import sys, heapq

input = sys.stdin.readline

n = int(input())
answer = list()

for _ in range(n):
    numbers = list(map(int, input().split()))
    for num in numbers:
        if len(answer) < n:
            heapq.heappush(answer, num)
            continue
        m = heapq.heappop(answer)
        if m < num:
            heapq.heappush(answer, num)
            continue
        heapq.heappush(answer, m)

print(answer[0])
