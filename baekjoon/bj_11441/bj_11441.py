import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
sum_arr = [0]

for a in arr:
    sum_arr.append(sum_arr[-1] + a)

answer = []

for _ in range(M):
    i, j = map(int, input().split())
    answer.append(sum_arr[j] - sum_arr[i - 1])

for a in answer:
    print(a)
