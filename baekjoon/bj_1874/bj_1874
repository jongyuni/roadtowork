import sys

N = int(input())
answer = []
stack = []
cnt = 0
flag = True

for _ in range(N):
  num = int(sys.stdin.readline().strip())
  
  while cnt < num:
    answer.append("+")
    cnt += 1
    stack.append(cnt)
    
  if stack[-1] == num and flag:
    answer.append("-")
    stack.pop()
  else:
    answer = ["NO"]
    flag = False

for msg in answer:
  print(msg)
