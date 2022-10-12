from collections import defaultdict
N = int(input())

owns = list(map(int, input().split()))
owns_dict = defaultdict(int)
M = int(input())

checks = list(map(int, input().split()))

answers = list()

for o in owns:
    owns_dict[o] += 1

for c in checks:
    if c in owns_dict:
        answers.append(owns_dict[c])
    else:
        answers.append(0)

for a in answers:
    print(a, end=' ')
