import sys

a, b = map(int, sys.stdin.readline().split())
answer = 0
num = [True] * (b - a + 1)

for i in range(2, int(b ** 0.5) + 1):
    d = i * i
    s = a // d
    if a % d != 0:
        s += 1
    for j in range(s, b // d + 1):
        num[j * d - a] = False

for n in num:
    if n:
        answer += 1

print(answer)
