import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
answer = 0
numbers.sort()
i, j = 0, N-1

while i < j:
    T = numbers[i] + numbers[j]
    if T == M:
        answer += 1
        i += 1
        j -= 1
    elif T > M:
        j -= 1
    elif T < M:
        i += 1

print(answer)
