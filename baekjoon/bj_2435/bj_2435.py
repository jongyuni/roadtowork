import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
tmp = 0
sum_arr = []

for i in range(K):
    tmp += arr[i]

sum_arr.append(tmp)

for i in range(K, N):
    t = sum_arr[-1] + arr[i] - arr[i - K]
    sum_arr.append(t)

print(max(sum_arr))
