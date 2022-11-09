import sys, heapq

answer = 0
N = int(input())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

newA = list()
newB = list()

for i in range(N):
    heapq.heappush(newA, (A[i], A[i]))
    heapq.heappush(newB, (-B[i], B[i]))

for i in range(N):
    a = heapq.heappop(newA)[1]
    b = heapq.heappop(newB)[1]
    answer += a * b

print(answer)
