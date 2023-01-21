import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
max_sum = 0
prev_sum = 0

for i in range(K):
    max_sum += arr[i]

prev_sum = max_sum

for j in range(N-K):
    prev_sum = prev_sum - arr[j] + arr[K+j]
    max_sum = max(max_sum, prev_sum)

print(max_sum)
