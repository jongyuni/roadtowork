import sys, heapq

N = int(input())
cards = list()
answer = 0

for _ in range(N):
    heapq.heappush(cards, int(sys.stdin.readline()))

while len(cards) > 1:
    i = heapq.heappop(cards)
    j = heapq.heappop(cards)
    heapq.heappush(cards, i + j)
    answer += i + j

print(answer)
