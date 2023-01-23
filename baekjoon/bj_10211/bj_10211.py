import sys

input = sys.stdin.readline

T = int(input())
answer = []

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    sum_arr = [arr[0]]

    for i in range(1, N):
        tmp = max(sum_arr[-1] + arr[i], arr[i])
        sum_arr.append(tmp)

    answer.append(max(sum_arr))

for a in answer:
    print(a)
