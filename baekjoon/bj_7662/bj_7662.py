import heapq
import sys
from collections import defaultdict

answer = []

N = int(sys.stdin.readline())

for _ in range(N):
    min_que = []
    max_que = []
    outcheck = defaultdict(int)

    M = int(sys.stdin.readline())
    for x in range(M):
        cmd, num = sys.stdin.readline().split()
        n = int(num)
        if cmd == 'I':
            heapq.heappush(min_que, (n, n))
            heapq.heappush(max_que, (-n, n))
            outcheck[n] += 1
        elif cmd == 'D' and n == 1:
            while max_que and not outcheck[max_que[0][1]]:
                heapq.heappop(max_que)
            if max_que:
                outcheck[max_que[0][1]] -= 1
                heapq.heappop(max_que)
        elif cmd == 'D' and n == -1:
            while min_que and not outcheck[min_que[0][1]]:
                heapq.heappop(min_que)
            if min_que:
                outcheck[min_que[0][1]] -= 1
                heapq.heappop(min_que)
        else:
            continue

    while min_que and not outcheck[min_que[0][1]]:
        heapq.heappop(min_que)
    while max_que and not outcheck[max_que[0][1]]:
        heapq.heappop(max_que)

    if not min_que or not max_que:
        answer.append("EMPTY")
    else:
        a = max_que[0][1]
        b = min_que[0][1]
        tmp = str(a) + ' ' + str(b)
        answer.append(tmp)

for ans in answer:
    print(ans)
