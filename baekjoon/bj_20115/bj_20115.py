import sys, heapq

input = sys.stdin.readline

n = int(input())
drinks = list(map(int, input().split()))
max_heap = []
min_heap = []

for drink in drinks:
    heapq.heappush(min_heap, drink)
    heapq.heappush(max_heap, (-drink, drink))

for _ in range(n - 1):
    a = heapq.heappop(min_heap)
    b = heapq.heappop(max_heap)[1]
    new = b + (a / 2)
    heapq.heappush(min_heap, new)
    heapq.heappush(max_heap, (-new, new))

answer = heapq.heappop(max_heap)[1]

if str(answer).endswith('5'):
    print(answer)
else:
    print(int(answer))
