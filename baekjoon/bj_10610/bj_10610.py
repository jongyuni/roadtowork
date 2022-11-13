import sys, heapq

nums = list(map(int, list(sys.stdin.readline().strip())))
answer = 0
heap = list()
three = 0
zero = 0

for n in nums:
    three += n
    if n == 0:
        zero += 1
    heapq.heappush(heap, (-n, n))

if three % 3 != 0 or zero == 0:
    answer = -1
else:
    tmp = ""
    while heap:
        t = heapq.heappop(heap)[1]
        tmp += str(t)
    answer = int(tmp)

print(answer)
