import sys, heapq

N = int(input())
answer = 0
times = list()
pe, ps = 0, 0

for _ in range(N):
    s, e = map(int, sys.stdin.readline().split())
    heapq.heappush(times, (e, s))

for _ in range(N):
    e, s = heapq.heappop(times)
    if s >= pe:
        answer += 1
        pe, ps = e, s

print(answer)
