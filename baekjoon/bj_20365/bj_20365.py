import sys

input = sys.stdin.readline

n = int(input())
orders = input().rstrip()
paints = {'B': 0, 'R': 0}
prev = ''

for order in orders:
    if order == prev:
        continue
    paints[order] += 1
    prev = order

answer = min(paints['B'], paints['R']) + 1
print(answer)
