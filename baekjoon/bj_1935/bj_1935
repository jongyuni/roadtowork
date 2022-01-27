import sys
N = int(input())
S = sys.stdin.readline().rstrip()
alpha = [0]*26

for i in range(N):
  n = int(input())
  alpha[i] = n
stack = []

for s in S:
  if 'A' <= s <= 'Z':
    stack.append(alpha[ord(s)-ord('A')])
  else:
    o2 = stack.pop()
    o1 = stack.pop()
    if s == "+":
      stack.append(o1+o2)
    elif s == "-":
      stack.append(o1-o2)
    elif s == "*":
      stack.append(o1*o2)
    elif s == "/":
      stack.append(o1/o2) 

print("{:.2f}".format(float(stack[0])))
