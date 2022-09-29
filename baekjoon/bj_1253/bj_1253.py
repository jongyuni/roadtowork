import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
answer = 0
numbers.sort()
goal = 0
i, j = 0, N - 1

for k in range(N):
    goal = numbers[k]
    i = 0
    j = N - 1
    while i < j:
        if numbers[i] + numbers[j] == goal:
            if i != k and j != k:
                answer += 1
                i = j
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1

        elif numbers[i] + numbers[j] > goal:
            j -= 1

        else:
            i += 1


print(answer)
