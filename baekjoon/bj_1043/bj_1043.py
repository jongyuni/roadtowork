import sys

n, m = map(int, sys.stdin.readline().split())
tmp = list(map(int, sys.stdin.readline().split()))
truth_num = tmp[0]
truth_people = list()
answer = 0

if truth_num != 0:
    truth_people = tmp[1:]

party_people = list()
for _ in range(m):
    tmp = list(map(int, sys.stdin.readline().split()))
    party_people.append(tmp[1:])

parent = [i for i in range(n + 1)]


def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a


for people in party_people:
    pivot = people[0]
    for i in range(1, len(people)):
        union(pivot, people[i])

for people in party_people:
    pivot = people[0]
    for t in truth_people:
        if find(pivot) == find(t):
            break
    else:
        answer += 1

print(answer)
