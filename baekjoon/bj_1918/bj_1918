import sys
S = sys.stdin.readline().rstrip()
answer = ""
stack = []

for s in S:
  if s.isalpha():
    answer += s
  elif s == ")":
    while True:
      i = stack.pop()
      if i == "(":
        break
      else:
        answer += i
  elif s == "*" or s == "/":
    while stack:
      i = stack.pop()
      if i == "*" or i =="/":
        answer += i
      else:
        stack.append(i)
        break
    stack.append(s)
  elif s == "+" or s == "-":
    while stack:
      i = stack.pop()
      if i == "(":
        stack.append(i)
        break
      else:
        answer += i
    stack.append(s)
  else:
    stack.append(s)

for s in stack[::-1]:
  answer += s

print(answer)

  
