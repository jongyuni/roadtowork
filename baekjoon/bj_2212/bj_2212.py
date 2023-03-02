import sys, heapq

input = sys.stdin.readline

n = int(input())
k = int(input())
sensors = list(map(int, input().split()))
sensors.sort()
distances = []
answer = 0

if n == 1:
    print(0)
else:
    for i in range(1, n):
        heapq.heappush(distances, sensors[i - 1] - sensors[i])

    for _ in range(k - 1):
        heapq.heappop(distances)

    while distances:
        answer += - heapq.heappop(distances)

    print(answer)
