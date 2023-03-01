import sys, heapq

input = sys.stdin.readline

n = int(input())
times = []
answer = []

for _ in range(n):
    s, e = map(int, input().split())
    times.append([s, e])

times.sort()
s, e = times[0]
heapq.heappush(answer, e)

for i in range(1, n):
    s, e = times[i]
    tmp = heapq.heappop(answer)
    if s < tmp:
        heapq.heappush(answer, tmp)
        heapq.heappush(answer, e)
    else:
        heapq.heappush(answer, e)

print(len(answer))
