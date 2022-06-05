import sys
sent = sys.stdin.readline().rstrip()
ans = []
flag = False
tmp = ""
answer = ""

for s in sent:
  if flag:
    if s == ">":
      tmp += s
      flag = False
      answer += tmp
      tmp = ""
      continue
    
    tmp += s
    continue
  
  else:
    if s == "<":
      tmp += s
      flag = True
      continue
    
    elif s == " ":
      tmp += s
      answer += tmp
      tmp = ""
      continue
    
    tmp = s + tmp
else:
  answer += tmp

print(answer)
