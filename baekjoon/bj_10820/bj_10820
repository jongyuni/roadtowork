import sys
answer = []

while True:
  S = sys.stdin.readline().rstrip('\n')
  tmp = [0] * 4
  if not S:
    break
  for s in S:
    if s.islower():
      tmp[0] += 1
    elif s.isupper():
      tmp[1] += 1
    elif s.isdigit():
      tmp[2] += 1
    elif s == " ":
      tmp[3] += 1
  tmp = list(map(str,tmp))
  answer.append(tmp)
  

for lst in answer:
  print(' '.join(lst))
