import sys

N = int(input())

numbers = list(map(int, sys.stdin.readline().split()))

M = int(input())

wants = list(map(int, sys.stdin.readline().split()))

numbers.sort()
answers = list()

for want in wants:
    start = 0
    end = len(numbers) - 1
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        if numbers[mid] == want:
            answer = 1
            break
        elif numbers[mid] > want:
            end = mid - 1
        else:
            start = mid + 1
    answers.append(answer)

for ans in answers:
    print(ans)
