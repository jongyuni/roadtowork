import sys

N = int(sys.stdin.readline())

s, e = 1, 1
answer = 1
T = 1

while s < N//2 + 1:
    T = (s + e) * (e - s + 1) // 2
    if T > N:
        s += 1
    elif T == N:
        answer += 1
        s += 1
        e += 1
    else: # T < N
        e += 1

print(answer)
