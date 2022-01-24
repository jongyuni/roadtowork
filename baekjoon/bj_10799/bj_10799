import sys
sent = sys.stdin.readline().rstrip()
answer = 0
lst = ""
stack = []

for s in sent:
  if s == "(":
    stack.append(s)
    
  elif s == ")":
    if lst == "(":
      stack.pop()
      answer += len(stack)
      
    else:
      stack.pop()
      answer += 1
  
  lst = s

print(answer)
