import sys

input = sys.stdin.readline

n, k = map(int, input().split())
childs = list(map(int, input().split()))
diffs = list()

for i in range(1, n):
    diffs.append(childs[i] - childs[i - 1])

diffs.sort()
print(sum(diffs[:n - k]))
