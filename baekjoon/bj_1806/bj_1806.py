import sys

N, S = map(int, sys.stdin.readline().split())
input_array = list(map(int, sys.stdin.readline().split()))
sum_array = [0] * (N + 1)

for i in range(1, N + 1):
    sum_array[i] = sum_array[i - 1] + input_array[i - 1]

start, end = 0, 0
min_distance = sys.maxsize

while start != N:
    if sum_array[end] - sum_array[start] >= S:
        min_distance = min(min_distance, end - start)
        start += 1
        continue

    if end != N:
        end += 1
        continue
    start += 1

print(0) if min_distance == sys.maxsize else print(min_distance)
