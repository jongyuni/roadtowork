import sys
S = sys.stdin.readline().rstrip()
stack = [-1]*26

for i, s in enumerate(S):
  if stack[ord(s)-ord('a')] == -1:
    stack[ord(s)-ord('a')] = i
  else:
    continue

for i in stack:
  print(i, end=' ')
