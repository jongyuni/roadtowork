import sys

input = sys.stdin.readline
n, m = map(int, input().split())
jip = [i for i in range(n + 1)]
answer = []


def union(a, b):
    ra = find(a)
    rb = find(b)
    if rb != ra:
        jip[rb] = ra


def find(a):
    if a == jip[a]:
        return a
    jip[a] = find(jip[a])
    return jip[a]


for _ in range(m):
    o, a, b = map(int, input().split())
    if o == 0:
        union(a, b)
        continue
    if find(a) == find(b):
        answer.append('YES')
    else:
        answer.append('NO')

for a in answer:
    print(a)
