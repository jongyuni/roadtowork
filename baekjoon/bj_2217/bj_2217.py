import sys

N = int(input())
weights = list()

for _ in range(N):
    weights.append(int(sys.stdin.readline()))

weights.sort(reverse=True)

for i in range(N):
    weights[i] = weights[i] * (i + 1)

print(max(weights))
