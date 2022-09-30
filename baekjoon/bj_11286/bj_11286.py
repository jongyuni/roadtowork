import sys
from queue import PriorityQueue

N = int(sys.stdin.readline())
que = PriorityQueue()
answer = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x != 0:
        que.put((abs(x),x))
    else:
        if que.empty():
            answer.append(0)
        else:
            answer.append(que.get()[1])

for a in answer:
    print(a, end='\n')
