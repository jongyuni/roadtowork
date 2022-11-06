import sys, heapq

N = int(input())
answer = 0
positive = list()
negative = list()
zero = 0
one = 0

for _ in range(N):
    n = int(sys.stdin.readline())
    if n > 1:
        heapq.heappush(positive, n * -1)
    elif n == 1:
        one += 1
    elif n == 0:
        zero += 1
    else:
        heapq.heappush(negative, n)

while len(positive) > 1:
    a = heapq.heappop(positive) * -1
    b = heapq.heappop(positive) * -1
    answer += a * b

if positive:
    answer += positive[0] * -1

answer += one

while len(negative) > 1:
    a = heapq.heappop(negative)
    b = heapq.heappop(negative)
    answer += a * b

if negative and zero == 0:
    answer += heapq.heappop(negative)

print(answer)
