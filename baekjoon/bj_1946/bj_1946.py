import sys, heapq

input = sys.stdin.readline
K = int(input())
answer = list()

for _ in range(K):
    N = int(input())
    nums = list()
    for _ in range(N):
        i, j = map(int, input().split())
        heapq.heappush(nums, (i, j))
    cur, top = heapq.heappop(nums)
    cnt = 1

    while nums:
        i, j = heapq.heappop(nums)
        if j < top:
            top = j
            cnt += 1
    answer.append(cnt)

for a in answer:
    print(a)
