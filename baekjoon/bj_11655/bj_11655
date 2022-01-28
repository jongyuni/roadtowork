import sys
answer = ""
S = sys.stdin.readline().rstrip()

for s in S:
  if 'a' <= s <= 'm':
    answer += chr(ord(s)+13)
  elif 'n' <= s <= 'z':
    answer += chr(ord(s)-13)
  elif 'A' <= s <= 'M':
    answer += chr(ord(s)+13)
  elif 'N' <= s <= 'Z':
    answer += chr(ord(s)-13)
  else:
    answer += s

print(answer)
