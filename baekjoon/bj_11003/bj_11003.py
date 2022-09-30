import sys
from collections import deque

N, L = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
answer = []
min_que = deque()
i = 0

while i < len(A): # 1 ~ N-1
    if not min_que:
        min_que.append((A[i], i))
        answer.append(min_que[0][0])
        i += 1
        continue

    if i - min_que[0][1] >= L: # 윈도우 사이즈를 벗어난 최솟값 제외
        min_que.popleft()
        continue

    if min_que[0][0] >= A[i]: # 현재 윈도우의 최솟값과 비교
        min_que = deque() # 최솟값 바꾸기
        min_que.append((A[i], i))

    else: # min_que[0][0] < A[i]
        while min_que[-1][0] >= A[i]:
            min_que.pop()
        min_que.append((A[i], i))

    answer.append(min_que[0][0])
    i += 1


for a in answer:
    print(a, end=' ')
