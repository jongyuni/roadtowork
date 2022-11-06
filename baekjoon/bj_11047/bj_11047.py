import sys

N, K = map(int, input().split())
changes = list()
answer = 0

for _ in range(N):
    changes.append(int(sys.stdin.readline()))

for i in range(-1, -N-1, -1):
    if K == 0:
        break
    c = K // changes[i]
    if c > 0:
        answer += c
        K = K % changes[i]

print(answer)
