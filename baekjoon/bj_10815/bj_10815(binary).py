N = int(input())

owns = list(map(int, input().split()))

M = int(input())

checks = list(map(int, input().split()))

answers = list()
owns.sort()

for c in checks:
    start = 0
    end = len(owns) - 1
    ans = 0
    while start <= end:
        if c == owns[start] or c == owns[end]:
            ans = 1
            break
        mid = (start + end) // 2
        if c == owns[mid]:
            ans = 1
            break
        elif c > owns[mid]:
            start = mid + 1
        else:
            end = mid - 1
    answers.append(ans)

for a in answers:
    print(a, end=' ')
