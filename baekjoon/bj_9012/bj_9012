import sys

N = int(input())
answer = []

for _ in range(N):
  brackets = sys.stdin.readline().strip()
  if len(brackets) % 2 != 0:
    answer.append("NO")
    continue
  stack = []
  flag = 1
  for s in brackets:
    if flag == 0:
      continue
    if s == "(":
      stack.append("(")
    elif s == ")":
      if stack:
        stack.pop()
      else:
        flag = 0
        continue
  else:
    if stack:
      flag = 0
    if flag == 1:
      answer.append("YES")
    else:
      answer.append("NO")
 
for s in answer:
  print(s)  
