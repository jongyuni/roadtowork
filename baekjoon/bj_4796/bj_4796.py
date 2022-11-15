import sys

input = sys.stdin.readline
answer = []

while True:
    L, P, V = map(int, input().split())
    tmp = 0
    if L == 0 and P == 0 and V == 0:
        break
    i = V // P
    tmp += i * L
    V = V % P
    tmp += min(V, L)
    answer.append(tmp)

for i in range(len(answer)):
    print("Case ", end="")
    print(i + 1, end="")
    print(": ", end="")
    print(answer[i])
