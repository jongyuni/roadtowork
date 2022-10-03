import heapq
import sys
less_list = []
more_list = []
answer = []

N = int(sys.stdin.readline())

for _ in range(N):
    t = int(sys.stdin.readline())

    if len(less_list) == len(more_list):
        heapq.heappush(less_list, (-t, t))
    else:
        heapq.heappush(more_list, (t, t))

    if more_list and less_list[0][1] > more_list[0][1]:
        less = heapq.heappop(less_list)[1]
        more = heapq.heappop(more_list)[1]
        heapq.heappush(less_list, (-more, more))
        heapq.heappush(more_list, (less, less))

    answer.append(less_list[0][1])

for a in answer:
    print(a)
