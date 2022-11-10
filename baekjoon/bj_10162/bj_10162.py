import sys

T = int(sys.stdin.readline())
times = [300, 60, 10]
answer = []

if T % 10 == 0:
    for time in times:
        i, j = divmod(T, time)
        if i > 0:
            T = j
        answer.append(i)

if not answer:
    answer = [-1]

for a in answer:
    print(a, end=' ')
