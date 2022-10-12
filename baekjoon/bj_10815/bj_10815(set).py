N = int(input())

owns = set(map(int, input().split()))

M = int(input())

checks = list(map(int, input().split()))

answers = list()

for c in checks:
    if c in owns:
        answers.append(1)
    else:
        answers.append(0)

for a in answers:
    print(a, end=' ')
