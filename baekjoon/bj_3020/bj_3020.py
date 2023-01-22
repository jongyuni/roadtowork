import sys

input = sys.stdin.readline

N, H = map(int, input().split())

even_caves = [0] * H
odd_caves = [0] * H
min_walls = sys.maxsize
min_ways = 0

for i in range(N):
    x = int(input())

    if i % 2 == 1:
        odd_caves[x - 1] += 1
        continue

    even_caves[x - 1] += 1

for i in range(H - 1, 0, -1):
    even_caves[i - 1] += even_caves[i]
    odd_caves[i - 1] += odd_caves[i]

for i in range(H):
    tmp = even_caves[i] + odd_caves[H - 1 - i]
    if tmp < min_walls:
        min_walls = tmp
        min_ways = 1
    elif tmp == min_walls:
        min_ways += 1

print(min_walls, min_ways)
b
