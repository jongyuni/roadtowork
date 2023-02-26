import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
pts = list(map(int, input().split()))
pts.sort()
t = 0

if n % 2 == 1:
    t = pts.pop()

pts = deque(pts)

while pts:
    a = pts.popleft()
    b = pts.pop()
    t = max(t, a + b)

print(t)
