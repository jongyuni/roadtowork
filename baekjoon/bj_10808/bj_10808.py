import sys
S = sys.stdin.readline().rstrip()
stack = [0]*26

for s in S:
  stack[ord(s)-ord('a')] += 1

for i in stack:
  print(i, end=' ')
