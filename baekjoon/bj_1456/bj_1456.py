import sys

a, b = map(int, sys.stdin.readline().split())
answer = 0

num = [i for i in range(10000001)]

for i in range(2, int(10000001 ** 0.5) + 1):
    if num[i] == 0:
        continue
    for j in range(i + i, 10000001, i):
        num[j] = 0

for i in range(2, 10000001):
    if num[i] == 0:
        continue
    tmp = num[i]
    while tmp <= b:
        tmp *= num[i]
        if a <= tmp <= b:
            answer += 1

print(answer)
