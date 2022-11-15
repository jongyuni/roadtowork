import sys

input = sys.stdin.readline
S = input().strip()
zero = 0
one = 0
pre = ''

for c in S:
    if not pre:
        pre = c
        continue
    if int(pre) != int(c):
        if int(pre):
            one += 1
        else:
            zero += 1
        pre = c

if int(pre):
    one += 1
else:
    zero += 1

print(min(one, zero))
