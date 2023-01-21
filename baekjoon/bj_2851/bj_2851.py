import sys

input = sys.stdin.readline
answer = 0
current_sum = 0

for _ in range(10):
    current_sum += int(input())

    if abs(current_sum - 100) <= abs(answer - 100):
        answer = current_sum

print(answer)
