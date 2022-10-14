import sys, bisect

T = int(input())
N = int(input())
A_arr = list(map(int, sys.stdin.readline().split()))
M = int(input())
B_arr = list(map(int, sys.stdin.readline().split()))

A_sum = list()
B_sum = list()
answer = 0
for i in range(N):
    total = 0
    for j in range(i, N):
        total += A_arr[j]
        A_sum.append(total)

for i in range(M):
    total = 0
    for j in range(i, M):
        total += B_arr[j]
        B_sum.append(total)

B_sum.sort()

for a in A_sum:
    l = bisect.bisect_left(B_sum, T - a)
    r = bisect.bisect_right(B_sum, T - a)
    answer += r - l

print(answer)
